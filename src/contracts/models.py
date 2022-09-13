from django.db import models
from django.contrib.auth import get_user_model


class Contract(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.client.email} - {self.amount}€'
