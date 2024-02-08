from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from calib_management.models import *
from calib_management.forms import PlaceForm, ProbeForm, ProbeUpdateForm, ServiceForm


class PlaceCreateView(CreateView):
    template_name = 'installation_create.html'
    model = Places
    form_class = PlaceForm
    success_url = '/installations-list/'


class PlaceUpdateView(UpdateView):
    template_name = 'installation_create.html'
    model = Places
    form_class = PlaceForm
    success_url = '/installations'


class PlaceListView(ListView):
    model = Places
    template_name = 'installations_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlaceDeleteView(DeleteView):
    model = Places
    template_name = 'installation_delete.html'
    success_url = '/installations-list/'


class ProbeListView(ListView):
    model = Probes
    template_name = 'probe_list.html'
    context_object_name = 'probes'  # Nazwa obiektu kontekstu przekazywanego do szablonu

    def get_queryset(self):
        return Probes.objects.all()


class ProbeCreateView(CreateView):
    model = Probes
    template_name = 'probe_create.html'
    form_class = ProbeForm
    success_url = '/'


class ProbeUpdateView(UpdateView):
    model = Probes
    template_name = 'probe_update.html'
    form_class = ProbeUpdateForm
    success_url = '/'


class ProbeDeleteView(DeleteView):
    model = Probes
    template_name = 'probe_delete.html'
    success_url = '/'


class ProbeDetailView(DetailView):
    model = Probes
    template_name = 'probe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        probe = self.get_object()

        # Pobranie wpisu z najwyższą datą next_service
        last_service = probe.services.order_by('-datetime').first()
        context['last_service'] = last_service

        return context


class ServiceCreateView(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'service_add.html'
    success_url = '/'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        probe = Probes.objects.get(id=pk)
        form.instance.probe = probe
        return super().form_valid(form)


class ServiceListView(ListView):
    model = Services
    template_name = 'service_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceDeleteView(DeleteView):
    model = Services
    template_name = 'service_delete.html'
    success_url = '/service-list/'


class ServiceUpdateView(UpdateView):
    model = Services
    form_class = ServiceForm
    template_name = 'service_add.html'
    success_url = '/service-list/'


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'service_detail.html'
    context_object_name = 'service'
