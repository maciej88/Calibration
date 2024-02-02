import uuid

from django.db import models


class Places(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Probes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=False)
    technology_id = models.CharField(max_length=128, unique=False)
    serial_number = models.CharField(max_length=128, unique=False)
    factory = models.CharField(max_length=128, unique=False)
    model = models.CharField(max_length=128, unique=False)
    setup_date = models.DateField(auto_now_add=True, editable=True) #jako data instalacji
    place = models.ManyToManyField('Places')
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    datetime = models.DateField(auto_now_add=True, editable=True)
    probe = models.ForeignKey(Probes, related_name='services', on_delete=models.CASCADE)
    next_service = models.DateField(verbose_name="Termin kolejnej obsługi:")
    # file = models.FileField(upload_to='#todo') # todo!!!!

    def __str__(self):
        return self.name

