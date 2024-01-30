import uuid

from django.db import models


class InstructionTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Instructions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    instruction_type = models.ForeignKey(InstructionTypes, on_delete=models.CASCADE)
    # file = models.FileField(upload_to='...', null=True, blank=True) # todo !!!

    def __str__(self):
        return self.name


class Places(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    datetime = models.DateTimeField(auto_now_add=True, editable=True)
    # file = models.FileField(upload_to='#todo') # todo!!!!

    def __str__(self):
        return self.name


class Probes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128, unique=False)
    technology_id = models.CharField(max_length=128, unique=False)
    serial_number = models.CharField(max_length=128, unique=False)
    factory = models.CharField(max_length=128, unique=False)
    model = models.CharField(max_length=128, unique=False)
    setup_date = models.DateTimeField(auto_now_add=True, editable=True) #jako data instalacji
    place = models.ManyToManyField('Places')
    description = models.TextField()
    instruction = models.ManyToManyField('Instructions')
    service = models.ForeignKey('Services', blank=True, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Overviews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    overview_date = models.DateTimeField(auto_now_add=True, editable=True)
    probe = models.ManyToManyField('Probes')
