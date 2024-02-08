from django import forms
from calib_management.models import Places, Probes, Services

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.')
    username = forms.CharField(max_length=30, required=True, help_text='Wymagane')
    password1 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło', 'type': 'password'})
    password2 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło', 'type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class LogoutForm(forms.Form):
    pass
