from django.contrib import admin

# Register your models here.
from calib_management.models import (
    InstructionTypes, Instructions, Places, Probes, Overviews, Services)

admin.site.register(InstructionTypes)
admin.site.register(Instructions)
admin.site.register(Places)
admin.site.register(Probes)
admin.site.register(Overviews)
admin.site.register(Services)
