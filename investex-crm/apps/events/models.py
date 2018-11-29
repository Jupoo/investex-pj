from django.db import models

from apps.core.models import GenericModel
from django.utils.translation import ugettext_lazy as _


class Event(GenericModel):
    EVENT_TYPE_DEPOSIT = 1
    EVENT_TYPE_WITHDRAWAL = 2

    EVENT_TYPES = (
        (EVENT_TYPE_DEPOSIT, 'deposit'),
        (EVENT_TYPE_WITHDRAWAL, 'withdrawal'),
    )

    event_type = models.PositiveIntegerField(verbose_name=_('event type'), choices=EVENT_TYPES,
                                             default=EVENT_TYPE_DEPOSIT)
    amount = models.DecimalField(verbose_name=_('amount'), max_digits=20, decimal_places=2, default=0)
    client = models.ForeignKey('clients.Client', related_name='events', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.get_event_type_display()}'

    class Meta:
        ordering = ('-created_at',)

    @property
    def get_full_name(self):
        return f'{self.client.account.first_name} {self.client.account.last_name}'

    @property
    def get_full_event(self):
        return f'{self.get_event_type_display().capitalize()} ${self.amount}'
