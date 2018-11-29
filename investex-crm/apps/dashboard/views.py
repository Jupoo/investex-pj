from django.views.generic import ListView
from django_tables2 import SingleTableMixin

from apps.events.models import Event
from apps.events.tables import EventsTable


class DashboardView(SingleTableMixin, ListView):
    table_class = EventsTable
    template_name = 'dashboard/dashboard.html'
    model = Event
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset()

