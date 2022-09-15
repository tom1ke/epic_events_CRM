from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'support_contact',
        'contract',
        'status',
        'attendees',
        'event_date',
        'date_created',
        'date_updated'
    )

admin.site.register(Event, EventAdmin)
