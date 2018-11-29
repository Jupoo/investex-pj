import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.core.managers import AccountManager


class GenericModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(
        verbose_name=_('created'),
        default=timezone.now, db_index=True)

    updated_at = models.DateTimeField(
        verbose_name=_('updated'),
        auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Account(GenericModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = AccountManager()

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __str__(self):
        return self.email
