from . import views as about_views
from django.urls import path


urlpatterns = [
    path('about/', about_views.AboutDetailView.as_view(), name='about'),
]