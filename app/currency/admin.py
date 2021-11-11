from currency.models import ContactUs, Rate, Source
from currency.resources import RateResource

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateTimeRangeFilter


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        ('created', DateTimeRangeFilter),
    )
    search_fields = (
        'buy',
        'sale',
        'source',
        'type',
    )
    readonly_fields = (
        'buy',
        'sale',
    )


admin.site.register(Rate, RateAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
    )
    list_filter = (
        'source_url',
        'name',
    )
    search_fields = (
        'source_url',
        'name',
    )
    readonly_fields = (
        'id',
    )


admin.site.register(Source, SourceAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
    )
    list_filter = (
        'email_from',
    )
    search_fields = (
        'email_from',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
