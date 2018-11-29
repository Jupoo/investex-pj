from django.views.generic import ListView
from django_tables2 import SingleTableMixin

from apps.clients.models import Client
from apps.clients.tables import ClientsTable


class ClientsView(SingleTableMixin, ListView):
    table_class = ClientsTable
    template_name = 'clients/clients.html'
    model = Client
    table_pagination = {"per_page": 20}

    def get_queryset(self):
        return super().get_queryset()
