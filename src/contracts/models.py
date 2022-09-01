from django.db import models
from django.contrib.auth import get_user_model


class Contract(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, related_name='contract_status')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)
    amount = models.FloatField
    payment_due = models.DateTimeField

    def __str__(self):
        return self.client
