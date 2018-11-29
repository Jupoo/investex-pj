from django.contrib import admin

from apps.tracking.models import PerDayTracking


@admin.register(PerDayTracking)
class PerDayTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'client')
