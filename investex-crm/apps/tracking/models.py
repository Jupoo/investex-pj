from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.managers import BulkInsertManager


class PerDayTracking(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_('report date'), db_index=True)
    updated_at = models.DateTimeField(verbose_name=_('updated time'), auto_now_add=True)
    leads = models.PositiveIntegerField(verbose_name=_('leads'), default=0)
    new_clients = models.PositiveIntegerField(verbose_name=_('new clients'), default=0)
    deposits = models.DecimalField(verbose_name=_('deposits sum'), max_digits=20, decimal_places=2, default=0)
    withdrawals = models.DecimalField(verbose_name=_('withdrawals sum'), max_digits=20, decimal_places=2, default=0)
    trading_volume = models.PositiveIntegerField(verbose_name=_('trading volume'), default=0)

    objects = BulkInsertManager()

    def __str__(self):
        return f'{self.date} - {self.client}'
