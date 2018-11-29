from django.contrib import admin

from apps.core.models import Account
from django.utils.translation import ugettext_lazy as _


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone', 'password',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
