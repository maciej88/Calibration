"""
URL configuration for calibration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calib_management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProbeListView.as_view(), name='probe_list'),
    path('installation-create/', PlaceCreateView.as_view(), name='place-create'),
    path('installations-list/', PlaceListView.as_view(), name='place-list'),
    path('installation-delete/<uuid:pk>/delete/', PlaceDeleteView.as_view(), name='place-delete'),
    path('installation-update/<uuid:pk>/update/', PlaceUpdateView.as_view(), name='place-update'),
    path('probe-create/', ProbeCreateView.as_view(), name='probe-create'),
    path('probe-update/<uuid:pk>/update/', ProbeUpdateView.as_view(), name='probe-update'),
    path('probe-delete/<uuid:pk>/delete/', ProbeDeleteView.as_view(), name='probe-delete'),
    path('probe-detail/<uuid:pk>', ProbeDetailView.as_view(), name='probe-detail'),
    path('add-service/<uuid:pk>/', ServiceCreateView.as_view(), name='add-service'),
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('service-delete/<uuid:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('service-update/<uuid:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service-detail/<uuid:pk>', ServiceDetailView.as_view(), name='service-detail'),
]
