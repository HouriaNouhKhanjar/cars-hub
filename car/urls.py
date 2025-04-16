from . import views as car_views
from django.urls import path

urlpatterns = [
    path('profile/', car_views.profile, name='profile'),
    path('cars-list/', car_views.cars_list, name='cars_list'),
    path('car-edit/', car_views.car_edit, name='car_edit'),
    path('liking-list/', car_views.liking_list, name='liking_list'),
    path('', car_views.index, name='home'),
]