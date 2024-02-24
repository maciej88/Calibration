from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from calib_management.models import Probes, Services, Places
from calib_management.forms import (
    PlaceForm, ProbeForm, ProbeUpdateForm, ServiceForm, UserUpdateForm, PassChangeForm,
    ServiceUpdateForm)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from .filters import ProbeFilter, ServiceFilter


# --- Place CRUD ---


# place create view:
class PlaceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'installation_create.html'
    model = Places
    form_class = PlaceForm
    success_url = '/installations-list/'


# place update view:
class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'installation_create.html'
    model = Places
    form_class = PlaceForm
    success_url = '/installations/'


# place list view:
class PlaceListView(LoginRequiredMixin, ListView):
    model = Places
    template_name = 'installations_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# place delete view:
class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Places
    template_name = 'installation_delete.html'
    success_url = '/installations-list/'


# --- Probe CRUD ---


# probe list view (main app view):
class ProbeListView(ListView):
    model = Probes
    template_name = 'probe_list.html'
    context_object_name = 'probes'

    # adding additional data to template: filter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProbeFilter(self.request.GET, queryset=self.get_queryset())
        return context


# probe create view
class ProbeCreateView(LoginRequiredMixin, CreateView):
    model = Probes
    template_name = 'probe_create.html'
    form_class = ProbeForm
    success_url = '/'


# probe update view
class ProbeUpdateView(LoginRequiredMixin, UpdateView):
    model = Probes
    template_name = 'probe_update.html'
    form_class = ProbeUpdateForm
    success_url = '/'


# probe delete view
class ProbeDeleteView(LoginRequiredMixin, DeleteView):
    model = Probes
    template_name = 'probe_delete.html'
    success_url = '/'


# probe create vew:
class ProbeDetailView(DetailView):
    model = Probes
    template_name = 'probe_detail.html'

    # expanding information: services to probes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        probe = self.get_object()

        # Pobranie wpisu z najwyższą datą next_service
        last_service = probe.services.order_by('-date_time').first()
        context['last_service'] = last_service

        return context


# --- Service CRUD ---

# service create view:
class ServiceCreateView(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'service_add.html'
    success_url = '/'

    # taking user id for create service:
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        pk = self.kwargs['pk']
        probe = Probes.objects.get(id=pk)
        form.instance.probe = probe
        return super().form_valid(form)


# service list view:
class ServiceListView(ListView):
    model = Services
    template_name = 'service_list.html'

    # adding additional data to template: filter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceFilter(self.request.GET, queryset=self.get_queryset())
        return context


# service delete view:
class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = 'service_delete.html'
    success_url = '/service-list/'


# service update view:
class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    form_class = ServiceUpdateForm
    template_name = 'service_add.html'
    success_url = '/service-list/'


# service detail view:
class ServiceDetailView(DetailView):
    model = Services
    template_name = 'service_detail.html'
    context_object_name = 'service'


# --- User CRU ---
# User create:
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# user logout:
class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')

    def post(self, request):
        return self.get(request)


# user update:
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    success_url = reverse_lazy('user-detail')
    form_class = UserUpdateForm

    # redirect after success user update:
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})

    # preventing to view other user via id in slug:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj:
            raise PermissionDenied
        return obj


# user detail view:
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'

    # preventing to view user detail for other user:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj:
            raise PermissionDenied
        return obj


# password change
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    model = User
    template_name = 'user_pass_change.html'
    form_class = PassChangeForm

    # redirect after success password change:
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.request.user.pk})

    # taking user id to success redirect to user details
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
