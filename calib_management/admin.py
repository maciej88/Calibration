from django.contrib import admin

# Register your models here.
from calib_management.models import (Places, Probes, Services)

admin.site.register(Places)
admin.site.register(Probes)
admin.site.register(Services)
