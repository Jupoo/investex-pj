from django.contrib import admin

from apps.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'amount', 'client')
    list_filter = ('event_type',)
