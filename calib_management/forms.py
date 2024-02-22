from django import forms
from calib_management.models import Places, Probes, Services
from django.contrib.auth.forms import PasswordChangeForm
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
        fields = ['name', 'date_time', 'next_service', 'description']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_time': forms.DateInput(attrs={'class': 'form-control',
                                               'placeholder': 'Select a date', 'type': 'date'}),
            'next_service': forms.DateInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Select a date', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


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


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Pierwsze imię")
    last_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.', label="Drugie imię")
    username = forms.CharField(max_length=30, required=True, help_text='Wymagane', label="Login")
    password1 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło', 'type': 'password'},)
    password2 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło', 'type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Wymagane.')
    username = forms.CharField(max_length=30, required=True, help_text='Wymagane')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['new_password1'].errorlist = {
    #         'required': 'To pole jest wymagane.',
    #         'password_too_short': 'Hasło musi zawierać co najmniej 8 znaków.',
    #         'password_common': 'Hasło nie może być powszechnie używanym hasłem.',
    #         'password_entirely_numeric': 'Hasło nie może składać się wyłącznie z cyfr.',
    #         'password_similar': 'Hasło nie może być zbyt podobne do innych Twoich danych osobowych.',
    #     }


class LogoutForm(forms.Form):
    pass
