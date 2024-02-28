from django.urls import path
from calib_management.views import *

from django.contrib.auth import views as auth_views

app_name = 'calib_management'

urlpatterns = [
    path('', ProbeListView.as_view(), name='probe-list'),
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
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url=''), name='login'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/password-change/', UserPasswordChangeView.as_view(), name='pass-change'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]