from django.conf import settings
from django.db import models
from django.utils import timezone
from ordered_model.models import OrderedModel

from apps.core.models import GenericModel
from django.utils.translation import ugettext_lazy as _

from apps.core.utils import nullable


class Tag(OrderedModel):
    title = models.CharField(verbose_name=_('title'), max_length=100)

    def __str__(self):
        return self.title

    class Meta(OrderedModel.Meta):
        pass


class Client(GenericModel):
    CLIENT_TYPE_SALES = 1
    CLIENT_TYPE_CLIENT = 2
    CLIENT_TYPE_IB = 3

    CLIENT_TYPES = (
        (CLIENT_TYPE_SALES, 'sales'),
        (CLIENT_TYPE_CLIENT, 'client'),
        (CLIENT_TYPE_IB, 'ib'),
    )

    account = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   verbose_name=_('account'),
                                   related_name='client',
                                   on_delete=models.CASCADE)
    client_type = models.PositiveIntegerField(verbose_name=_('type'), choices=CLIENT_TYPES, default=CLIENT_TYPE_CLIENT)
    account_dashboard_uid = models.CharField(verbose_name=_('account dashboard UUID'), max_length=36, blank=True)
    ib = models.ForeignKey('self', verbose_name=_('client IB'), related_name='ibs', on_delete=models.DO_NOTHING,
                           **nullable)
    sales = models.ForeignKey('self', verbose_name=_('account manager'), related_name='sales_managers',
                              on_delete=models.DO_NOTHING, **nullable)
    nav = models.DecimalField(verbose_name=_('nav'), max_digits=20, decimal_places=2, default=0)
    trading_volume = models.PositiveIntegerField(verbose_name=_('trading volume'), default=0)
    deposits = models.DecimalField(verbose_name=_('deposits sum'), max_digits=20, decimal_places=2, default=0)
    withdrawals = models.DecimalField(verbose_name=_('withdrawals sum'), max_digits=20, decimal_places=2, default=0)
    registered_date = models.DateTimeField(verbose_name=_('registered date'), **nullable)
    last_login = models.DateTimeField(verbose_name=_('last login'), **nullable)
    last_contact = models.DateTimeField(verbose_name=_('last contact'), **nullable)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.get_client_type_display()}] - {self.account.email}'

    @property
    def get_first_name(self):
        return f'{self.account.first_name}'

    @property
    def get_last_name(self):
        return f'{self.account.last_name}'

    @property
    def get_email(self):
        return f'{self.account.email}'

    @property
    def get_phone(self):
        return f'{self.account.phone}'

    @property
    def get_full_name(self):
        return f'{self.account.first_name} {self.account.last_name}'

    def is_contacted(self):
        if 'Contacted' in self.tags.values_list('title', flat=True):
            return True

    def is_deposited(self):
        if 'Funded' in self.tags.values_list('title', flat=True):
            return True

    def is_vip(self):
        if 'VIP' in self.tags.values_list('title', flat=True):
            return True


class Channel(OrderedModel):
    title = models.CharField(verbose_name=_('title'), max_length=100)

    def __str__(self):
        return self.title

    class Meta(OrderedModel.Meta):
        pass


class Comment(GenericModel):
    channel = models.ForeignKey(Channel, related_name='channel_comments', on_delete=models.DO_NOTHING)
    client = models.ForeignKey('clients.Client', related_name='comments', on_delete=models.DO_NOTHING)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.channel}: {self.client}'


class CommentFile(GenericModel):
    file = models.FileField(upload_to='comment_files/%Y/%m/%d/')
    comment = models.ForeignKey(Comment, related_name='files', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.file.name
