"""
URL configuration for carshub project.
The `urlpatterns` list routes URLs to views.
"""
from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include
from errors import views as error_views  # adjust to your app name

handler400 = error_views.error_400
handler403 = error_views.error_403
handler404 = error_views.error_404
handler500 = error_views.error_500

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include("about.urls"), name="about-urls"),
    path('', include("car.urls"), name="car-urls"),
]
