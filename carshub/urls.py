"""
URL configuration for carshub project.

The `urlpatterns` list routes URLs to views.
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('car/', include('car.urls'))
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
    path('forbiden/', error_views.forbiden),
    path('bad-request/', error_views.bad_request_view),
    path('crash/', error_views.crash_view),
    path('not-found/', error_views.not_found),
    path('', include("car.urls"), name="car-urls"),
]
