from django.contrib import admin

# Register your models here.
from calib_management.models import (
    InstructionTypes, Instructions, Places, Services, Probe, Overviews)

admin.site.register(InstructionTypes)
admin.site.register(Instructions)
admin.site.register(Places)
admin.site.register(Services)
admin.site.register(Probe)
admin.site.register(Overviews)
