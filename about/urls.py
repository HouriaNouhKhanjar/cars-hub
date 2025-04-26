from . import views as about_views
from django.urls import path


urlpatterns = [
    path('profile/', about_views.AboutDetailView.as_view(), name='about'),
]