import itertools

import django_tables2 as tables
from django.utils.html import format_html

from .models import Client
from django.utils.translation import ugettext_lazy as _


class ClientsTable(tables.Table):
    id = tables.Column()
    get_full_name = tables.Column(_('client name'), order_by=("account__first_name", "account__last_name"))
    get_email = tables.Column(_('email'), order_by='account__email')
    get_phone = tables.Column(_('phone'), order_by='account__phone')
    is_contacted = tables.Column(_('cont.'), empty_values=(), orderable=False)
    is_deposited = tables.Column(_('depos.'), empty_values=(), orderable=False)
    is_vip = tables.Column(_('vip'), empty_values=(), orderable=False)
    registered_date = tables.Column(_('registered'), default='n/a')
    last_login = tables.Column(_('last login'), default='n/a')

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

    def render_is_contacted(self, value):
        return self.get_checkbox(value)

    def render_is_deposited(self, value):
        return self.get_checkbox(value)

    def render_is_vip(self, value):
        return self.get_checkbox(value)

    class Meta:
        model = Client
        template_name = "django_tables2/no_bootstrap.html"
        fields = (
            'id', 'get_full_name', 'get_email', 'get_phone',
            'is_contacted', 'is_deposited', 'is_vip', 'registered_date', 'last_login'
        )
