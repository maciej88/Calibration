from django import forms
from calib_management.models import Places, Probes, Services


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = '__all__'


class ProbeForm(forms.ModelForm):
    class Meta:
        model = Probes
        fields = [
            'name', 'technology_id', 'serial_number', 'factory', 'probe_model', 'setup_date',
            'description', 'place']
        widgets = {
            'name': forms.TextInput(),
            'technology_id': forms.TextInput(),
            'serial_number': forms.TextInput(),
            'factory': forms.TextInput(),
            'probe_model': forms.TextInput(),
            'setup_date': forms.DateInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Select a date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'place': forms.Select(attrs={'class': 'form'})
        }


class ProbeUpdateForm(forms.ModelForm):
    class Meta:
        model = Probes
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'datetime', 'next_service', 'description']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'datetime': forms.DateInput(attrs={'class': 'form-control',
                                               'placeholder': 'Select a date', 'type': 'date'}),
            'next_service': forms.DateInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Select a date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
