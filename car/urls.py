from . import views as car_views
from django.urls import path

urlpatterns = [
    path('', car_views.index, name='home'),
]