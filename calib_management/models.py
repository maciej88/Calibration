import uuid

from django.contrib.auth.models import User
from django.db import models

SERVICE_TYPES = (
    ('Kalibracja', 'Kalibracja'),
    ('Konserwacja', 'Konserwacja'),
    ('Montaż', 'Montaż'),
    ('Czyszczenie', 'Czyszczenie'),
    ('Justowanie', 'Justowanie'),
    ('Wzorcowanie', 'Wzorcowanie')
)


class Places(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=True, verbose_name='Obiekt: ')

    def __str__(self):
        return self.name


class Probes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=False, verbose_name='Nazwa:')
    technology_id = models.CharField(max_length=128,
                                     unique=False, verbose_name='Numer technologiczny:')
    serial_number = models.CharField(max_length=128,
                                     unique=False, verbose_name='Numer seryjny:')
    factory = models.CharField(max_length=128, unique=False, verbose_name='Producent: ')
    probe_model = models.CharField(max_length=128, unique=False, verbose_name='Model: ')
    setup_date = models.DateField(editable=True, verbose_name='Data montażu: ') #jako data instalacji
    place = models.ForeignKey('Places', verbose_name='Instalacja: ',
                              on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name='Opis: ')
    status = models.BooleanField(default=True, verbose_name='Czy sprawna:')

    def __str__(self):
        return self.name

    def get_latest_service(self):
        return self.services.order_by('-date_time').first()


class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(choices=SERVICE_TYPES, verbose_name='Rodzaj obsługi:')
    date_time = models.DateField(editable=True, verbose_name='Data wykonania:')
    probe = models.ForeignKey(Probes, related_name='services',
                              on_delete=models.CASCADE, verbose_name='Obsługiwane urządzenie:')
    next_service = models.DateField(verbose_name="Termin kolejnej obsługi:")
    description = models.TextField(max_length=512, blank=True, verbose_name='Opis wykonanych czynności:')
    added_by = models.ForeignKey(User, verbose_name='Dodano przez:', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

