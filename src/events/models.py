from django.db import models
from django.contrib.auth import get_user_model

from clients.models import Client


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL)
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField
    attendees = models.IntegerField
    event_date = models.DateTimeField
    notes = models.TextField(max_length=2500)
