from django.views.generic import ListView
from django_tables2 import SingleTableMixin

from apps.events.models import Event
from apps.events.tables import EventsTable


class EventsView(SingleTableMixin, ListView):
    table_class = EventsTable
    template_name = 'clients/clients.html'
    model = Event
    table_pagination = {"per_page": 20}

    def get_queryset(self):
        return super().get_queryset()
