from django import forms
from calib_management.models import Places, Probes, Services
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# place form for place create view:
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = '__all__'


# probe form for probe create view
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
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'place': forms.Select(attrs={'class': 'form'})
        }


# probe update for probe update view:
class ProbeUpdateForm(forms.ModelForm):
    class Meta:
        model = Probes
        fields = '__all__'


# probe service form for service create
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'date_time', 'next_service', 'description']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_time': forms.DateInput(attrs={'class': 'form-control',
                                               'placeholder': 'Select a date', 'type': 'date'}),
            'next_service': forms.DateInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Select a date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


# probe service update form:
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'date_time', 'next_service', 'description', 'added_by']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_time': forms.DateInput(attrs={'class': 'form-control',
                                                'placeholder': 'Select a date', 'type': 'date'}),
            'next_service': forms.DateInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Select a date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'added_by': forms.Select(attrs={'class': 'form-control', 'placeholder': ''})
        }


# user creation form for user register:
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Pierwsze imię")
    last_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Drugie imię")
    username = forms.CharField(max_length=30, required=True, help_text='Wymagane', label="Login")
    password1 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło', 'type': 'password'},)
    password2 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło', 'type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


# user update form (no password):
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Pierwsze imię:")
    last_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Drugie imię:")
    username = forms.CharField(max_length=30, required=True, help_text='Wymagane', label="Login")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


# user password update form:
class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Stare hasło", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Stare hasło'}))
    new_password1 = forms.CharField(label="Nowe hasło", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Nowe hasło'}))
    new_password2 = forms.CharField(label="Powtórz nowe hasło", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Powtórz nowe hasło'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(user, *args, **kwargs)


# user logout form (must bee pass):
class LogoutForm(forms.Form):
    pass
