from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from apps.clients.forms import ClientAdminForm
from apps.clients.models import Client, Comment, Channel, CommentFile, Tag
from apps.events.models import Event


class EventInline(admin.TabularInline):
    model = Event
    extra = 0
    max_num = 0
    readonly_fields = ('created_at', 'event_type', 'amount', 'client')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    max_num = 0
    readonly_fields = ('created_at', 'channel', 'text', 'client')


@admin.register(Tag)
class TagAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ('client_type',)
    form = ClientAdminForm
    inlines = [EventInline, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'client')


@admin.register(Channel)
class ChannelAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')


@admin.register(CommentFile)
class CommentFileAdmin(admin.ModelAdmin):
    pass
