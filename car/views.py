from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Load the Homepage
    """
    return render(request, 'car/index.html')

def profile(request):
    """
    Manage profile page
    """
    return render(request, 'profile/index.html')

def cars_list(request):
    """
    Display users cars list
    """
    return render(request, 'profile/cars-list.html')

def car_edit(request):
    """
    Manage users car
    """
    return render(request, 'profile/cars-edit.html')

def liking_list(request):
    """
    display users liking
    """
    return render(request, 'profile/liking-list.html')