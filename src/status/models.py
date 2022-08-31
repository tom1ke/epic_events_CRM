from tkinter import CASCADE
from django.db import models

from contracts.models import Contract
from events.models import Event


class Status(models.Model):
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    status = models.BooleanField()