from . import views as car_views
from django.urls import path


urlpatterns = [
    path('profile/', car_views.profile, name='profile'),
    path('cars-list/', car_views.CarListView.as_view(), name='car_list'),
    path('add/', car_views.CarCreateView.as_view(), name='car_add'),
    path('liking-list/', car_views.liking_list, name='liking_list'),
    path('', car_views.index, name='home'),
]