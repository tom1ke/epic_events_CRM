from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    support_contact = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, related_name='event_status')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField
    event_date = models.DateTimeField
    notes = models.TextField(max_length=2500)

    def __str__(self):
        return self.client
