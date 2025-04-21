from . import views as car_views
from django.urls import path


urlpatterns = [
    path('profile/', car_views.profile, name='profile'),
    path('cars-list/', car_views.CarListView.as_view(), name='car_list'),
    path('add/', car_views.CarCreateView.as_view(), name='car_add'),
    path('car-edit/<int:pk>/', car_views.CarUpdateView.as_view(),
         name='car_edit'),
    path('car/image/<int:pk>/delete/', car_views.delete_car_image,
         name='delete_car_image'),
    path('car-delete/<int:pk>/', car_views.delete_car,
         name='car_delete'),
    path('likes-list/', car_views.likes_list, name='likes_list'),
    path('', car_views.index, name='home'),
]