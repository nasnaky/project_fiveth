from django.contrib import admin
from .models import CAMERA,HUMIDITY,TEMPERATURE,REMNANT_W

admin.site.register(CAMERA)
admin.site.register(TEMPERATURE)
admin.site.register(HUMIDITY)
admin.site.register(REMNANT_W)
