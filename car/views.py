from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .forms import UserForm, ProfileForm, CarForm
from .models import UserProfile
from .models import Car, Category, CarImage


# Create your views here.
def index(request):
    """
    Load the Homepage
    """
    return render(request, 'car/index.html')


@login_required
def profile(request):
    """
    Manage profile page
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


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'profile/cars-list.html'
    context_object_name = 'cars'
    paginate_by = 10 

    def get_queryset(self):
        queryset = Car.objects.filter(owner=self.request.user)

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
        context['categories'] = Category.objects.all()
     
        # Add search query to preserve the search term
        context['search'] = self.request.GET.get('search', '')
    
        # Add selected category to filter
        context['selected_category'] = self.request.GET.get('category', '')

        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'profile/add-car.html'
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


@login_required
def liking_list(request):
    """
    display users liking
    """
    return render(request, 'profile/liking-list.html')