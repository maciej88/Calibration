import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, FilterSet
from .models import Probes, Services


class ProbeFilter(django_filters.FilterSet):
    probe_from_date = DateFilter(field_name="setup_date", lookup_expr="gte", label='Montaż od daty:',
                                 widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    probe_to_date = DateFilter(field_name="setup_date", lookup_expr="lte", label="Montaż do daty:",
                               widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    serv_from_date = DateFilter(field_name="next_service", lookup_expr="gte", label="Serwis od:",
                                widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    serv_to_date = DateFilter(field_name="next_service", lookup_expr="lte", label="Serwis do:",
                              widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))

    class Meta:
        model = Probes
        fields = '__all__'
        exclude = ['id', 'probe_from_date', 'probe_to_date', 'serv_from_date', 'serv_to_date']


class ServiceFilter(FilterSet):
    serv_from_date = DateFilter(field_name="date_time", lookup_expr="gte", label="wykonanie od:",
                                widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    serv_to_date = DateFilter(field_name="date_time", lookup_expr="lte", label="Wykonanie do:",
                              widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    next_serv_from = DateFilter(field_name="next_service", lookup_expr="lte", label="Kolejna obsługa od:",
                              widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    next_serv_to = DateFilter(field_name="next_service", lookup_expr="lte", label="Kolejna obsługa do:",
                              widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))

    class Meta:
        model = Services
        fields = '__all__'
        exclude = ['id', 'serv_from_date', 'serv_to_date', 'next_serv_from', 'next_serv_to']