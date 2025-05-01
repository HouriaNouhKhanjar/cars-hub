from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils.timesince import timesince
from django.urls import reverse_lazy
from django.core.cache import cache
from django.utils.timezone import now
from django.db.models import Q
from django.contrib import messages
from .forms import UserForm, ProfileForm, CarForm
from .models import UserProfile, Car, Category, CarImage, Comment


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


@login_required
def profile(request):
    """
    Display the profile of the authenticated user to edit.

    **Context**

    ``user_form``
        An instance of :form:`car.UserForm`
    ``profile_form``
        An instance of :form:`car.ProfileForm`

    **Template:**

    :template:`profile/index.html`
    """
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(
                    request, messages.SUCCESS,
                    'Profile was successfuly updated.'
            )
            return redirect('profile')

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'profile/index.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@method_decorator(cache_page(60 * 15), name='dispatch')
class CarListView(ListView):
    """
    Returns all published cars in :model:`car.Car`
    and displays them in a page of nine cars.
    **Context**

    ``queryset``
        All published instances of :model:`car.Car`

    ``paginate_by``
        Number of cars per page.

    **Template:**

    ``Homepage_template``
        :template:`car/index.html`
    """
    model = Car
    context_object_name = 'cars'
    template_name = 'car/index.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Car.objects.select_related('category', 'owner') \
                   .prefetch_related('images') \
                   .filter(approved=1)

        # Search functionality based on title or model or brand
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(model__icontains=search_query) |
                Q(brand__icontains=search_query)
            )

        # Filter by category
        category_filter = self.request.GET.get('category', '')
        if category_filter:
            queryset = queryset.filter(category__id=category_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add a list of categories to filter by
        categories = cache.get('cached_categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('cached_categories', categories, 60 * 10)
        context['categories'] = categories

        # Add search query to preserve the search term
        context['search'] = self.request.GET.get('search', '')

        # Add selected category to filter
        context['selected_category'] = self.request.GET.get('category', '')

        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class UserCarListView(LoginRequiredMixin, ListView):
    """
    Returns all user cars in :model:`car.Car`
    and displays them in a cars list page of nine cars.
    **Context**

    ``queryset``
        All instances of :model:`car.Car` filtered by request.user

    ``paginate_by``
        Number of cars per page.

    **Template:**

    ``Profile_template``
        :template:`profile/cars-list.html`
    """
    model = Car
    context_object_name = 'cars'
    template_name = 'profile/cars-list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Car.objects.all()
        queryset = queryset.filter(owner=self.request.user)

        # Search functionality based on title or model or brand
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(model__icontains=search_query) |
                Q(brand__icontains=search_query)
            )

        # Filter by category
        category_filter = self.request.GET.get('category', '')
        if category_filter:
            queryset = queryset.filter(category__id=category_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add a list of categories to filter by
        categories = cache.get('cached_categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('cached_categories', categories, 60 * 10)
        context['categories'] = categories

        # Add search query to preserve the search term
        context['search'] = self.request.GET.get('search', '')

        # Add selected category to filter
        context['selected_category'] = self.request.GET.get('category', '')

        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    """
    Display car form page for create.

    **Context**

    ``form``
        An instance of :form:`car.CarForm`

    **Template:**

    :template:`profile/car-form.html`
    """
    model = Car
    form_class = CarForm
    template_name = 'profile/car-form.html'
    success_url = reverse_lazy('car_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        images = self.request.FILES.getlist('images')
        for img in images:
            CarImage.objects.create(car=self.object, image=img)
        messages.add_message(
                    self.request, messages.SUCCESS,
                    'Car was successfuly added.'
            )
        return response


class CarUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    """
    Display car form page for update.

    **Context**

    ``car``
        An instance of :model:`car.Car`
    ``edit_mode``
        True
    ``car_images``
        A list of image instance :model:`car.CarImage`
    ``form``
        An instance of :form:`car.CarForm`

    **Template:**

    :template:`profile/car-form.html`
    """
    model = Car
    form_class = CarForm
    template_name = 'profile/car-form.html'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_mode'] = True
        # access related CarImage
        context['car_images'] = self.object.images.all()
        return context

    def form_valid(self, form):
        images = self.request.FILES.getlist('images')
        for img in images:
            CarImage.objects.create(car=self.object, image=img)
        messages.success(self.request, "Car updated successfully!")
        return super().form_valid(form)


class CarDetailView(DetailView):
    """
    Display an individual :model:`car.Car`.

    **Context**

    ``car``
        An instance of :model:`car.Car`.

    **Template:**

    :template:`car/car-detail.html`
    """
    model = Car
    template_name = 'car/car-detail.html'
    context_object_name = 'car'

    def get_object(self, queryset=None):
        queryset = Car.objects.select_related('owner', 'category')\
                   .prefetch_related(
                       'images',
                       'likes',
                       'comments__user__user_profile')
        return super().get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context


@login_required
def delete_car(request, pk):
    """
    Delete an individual car.

    **args**

    ``pk``
        The instance id of :model:`car.Car` to delete.
    """
    if request.method not in ["POST", "DELETE"]:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    car = get_object_or_404(Car, pk=pk)

    # Check if the logged-in user is the owner of the related car
    if car.owner != request.user:
        return JsonResponse({'error': 'Forbidden'}, status=403)

    try:
        car.delete()
        messages.success(request, "Car deleted from Cloudinary successfully.")
        return JsonResponse({'success': True})
    except Exception as e:
        messages.error(request, f"Car deletion failed: {e}")
        return JsonResponse({'error': f'Car deletion failed: {e}'},
                            status=500)


@login_required
def delete_car_image(request, pk):
    """
    Delete an individual image.

    **args**

    ``pk``
        The instance id of :model:`car.CarImage` to delete.
    """
    if request.method not in ["POST", "DELETE"]:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    car_image = get_object_or_404(CarImage, pk=pk)

    # Check if the logged-in user is the owner of the related car
    if car_image.car.owner != request.user:
        return JsonResponse({'error': 'Forbidden'}, status=403)

    try:
        car_image.delete()
        messages.success(request,
                         "Image deleted from Cloudinary successfully.")
        return JsonResponse({'success': True})
    except Exception as e:
        messages.error(request, f"Cloudinary image deletion failed: {e}")
        return JsonResponse({'error': f'Cloudinary deletion failed: {e}'},
                            status=500)


@login_required
def toggle_like(request, pk):
    """
    Like or dislike a car.

    **args**

    ``pk``
        The id of instance of :model:`car.Car` to be like/dislike.
    """
    if request.method == "POST":
        car = get_object_or_404(Car, pk=pk)

        if request.user in car.likes.all():
            car.likes.remove(request.user)
            liked = False
        else:
            car.likes.add(request.user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'total_likes': car.total_likes(),
        })

    return HttpResponseForbidden()


class UserLikedCarsView(LoginRequiredMixin, ListView):
    """
    Returns all cars in :model:`car.Car`
    that are liked by request.user
    and displays them in a page of ten likes.
    **Context**

    ``queryset``
        All car instances of :model:`car.Car` filtered by request.user
    ``paginate_by``
        Number of cars per page.

    **Template:**

    :template:`profile/likes-list.html`
    """
    model = Car
    template_name = 'profile/likes-list.html'
    context_object_name = 'cars'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        queryset = Car.objects.filter(likes=user)

        return queryset


@login_required
def add_comment(request):
    """
    Save a comment on car.

    **request**

    ``content``
        User comment as a text.
    ``car_id``
        Car id that the user want to comment on.
    ``user``
        The authenticated user
    """
    if request.method not in ["POST"]:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        content = request.POST.get('content', '').strip()
        car_id = request.POST.get('car_id')
        if not content:
            return JsonResponse({'error': 'Comment cannot be empty.'},
                                status=400)
        car = get_object_or_404(Car, pk=car_id)
        comment = Comment.objects.create(user=request.user, car=car,
                                         content=content)

        image = comment.user.user_profile.image_url
        print(image)
        return JsonResponse({
            'id': comment.id,
            'user': comment.user.username,
            'image_url': image,
            'content': comment.content,
            'created': timesince(comment.created, now()) + " ago",
            'count': car.comments.count()
        })
    except Exception as e:
        return JsonResponse({'error': f'Comment update failed: {e}'},
                            status=500)


@login_required
def edit_comment(request, pk):
    """
    Update an individual comment.

    **args**

    ``pk``
        The instance id of :model:`car.Comment` to edit.
    """
    if request.method not in ["POST"]:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if comment.user != request.user:
        return JsonResponse({'error': 'Forbidden'}, status=403)
    try:
        content = request.POST.get('content', '').strip()
        if not content:
            return JsonResponse({'error': 'Comment cannot be empty.'},
                                status=400)
        comment.content = content
        comment.save()
        return JsonResponse({'success': True,
                             'content': comment.content,
                             'created': f"{timesince(comment.updated, now())}\
                                          ago"
                             })
    except Exception as e:
        return JsonResponse({'error': f'Comment update failed: {e}'},
                            status=500)


@login_required
def delete_comment(request, pk):
    """
    Delete an individual comment.

    **args**

    ``pk``
        The instance id of :model:`car.Comment` to delete.
    """
    if request.method not in ["POST", "DELETE"]:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if comment.user != request.user:
        return JsonResponse({'error': 'Forbidden'}, status=403)
    try:
        comment.delete()
        messages.success(request, "Comment was deleted successfully.")
        return JsonResponse({'success': True})
    except Exception as e:
        messages.error(request, f"Comment deletion failed: {e}")
        return JsonResponse({'error': f'Comment deletion failed: {e}'},
                            status=500)
