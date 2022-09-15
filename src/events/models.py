from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    support_contact = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    contract = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE, related_name='event_contract')
    status = models.ForeignKey('status.Status', on_delete=models.SET_NULL, null=True, related_name='event_status')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    attendees = models.PositiveIntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=2500)

    def __str__(self):
        return f'{self.client.email} - {self.event_date}'
