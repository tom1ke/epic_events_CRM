from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'company_name',
        'sales_contact',
        'first_name',
        'last_name',
        'phone',
        'mobile',
        'date_created',
        'date_updated'
    )
    
    
admin.site.register(Client, ClientAdmin)
