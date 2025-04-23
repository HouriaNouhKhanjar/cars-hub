from . import views as car_views
from django.urls import path


urlpatterns = [
    path('profile/', car_views.profile, name='profile'),
    path('profile/cars-list/', car_views.CarListView.as_view(), name='car_list'),
    path('car-add/', car_views.CarCreateView.as_view(), name='car_add'),
    path('car-edit/<int:pk>/', car_views.CarUpdateView.as_view(),
         name='car_edit'),
    path('car/image/<int:pk>/delete/', car_views.delete_car_image,
         name='delete_car_image'),
    path('car-delete/<int:pk>/', car_views.delete_car,
         name='car_delete'),
    path('car-detail/<int:pk>/', car_views.CarDetailView.as_view(),
         name='car_detail'),
    path('cars/<int:pk>/like/', car_views.toggle_like,
         name='toggle_like'),
    path('comments/add/', car_views.add_comment, 
         name='add_comment'),
    path('comments/<int:pk>/edit/', car_views.edit_comment, 
         name='edit_comment'),
    path('comments/<int:pk>/delete/', car_views.delete_comment,
         name='delete_comment'),
    path('profile/likes-list/', car_views.likes_list, name='likes_list'),
    path('', car_views.CarListView.as_view(), name='home'),
]