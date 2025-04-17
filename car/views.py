from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import UserProfile


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

@login_required
def cars_list(request):
    """
    Display users cars list
    """
    return render(request, 'profile/cars-list.html')

@login_required
def car_edit(request):
    """
    Manage users car
    """
    return render(request, 'profile/cars-edit.html')

@login_required
def liking_list(request):
    """
    display users liking
    """
    return render(request, 'profile/liking-list.html')