from django.contrib import admin

from webapp.models import SensorData


class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'signal', 'door_open', 'motion_sensed']

admin.site.register(SensorData, SensorDataAdmin)