from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'sales_contact',
        'signed',
        'amount',
        'payment_due',
        'date_created',
        'date_updated'
    )


admin.site.register(Contract, ContractAdmin)
