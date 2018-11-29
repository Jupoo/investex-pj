import itertools

import django_tables2 as tables
from django.utils.html import format_html

from apps.events.models import Event
from django.utils.translation import ugettext_lazy as _


class EventsTable(tables.Table):
    created_at = tables.DateTimeColumn(format='H:i', default='n/a', verbose_name=_('time'))
    get_full_event = tables.Column(_('event'), order_by='amount')
    get_full_name = tables.Column(_('client'), order_by=("client__account__first_name", "client__account__last_name"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count(start=1)

    def render_id(self):
        return f'{next(self.counter)}'

    @staticmethod
    def get_checkbox(value):
        if value:
            value = '<div class="table__check"><span class="icon--check"></span></div>'
        else:
            value = '<div class="table__check table--check-switchedoff"><span class="icon--check"></span></div>'
        return format_html(value)

    def render_event(self, value):
        return self.get_checkbox(value)

    def render_is_deposited(self, value):
        return self.get_checkbox(value)

    def render_is_vip(self, value):
        return self.get_checkbox(value)

    class Meta:
        model = Event
        template_name = "django_tables2/no_bootstrap.html"
        fields = (
            'created_at', 'get_full_event', 'get_full_name'
        )
