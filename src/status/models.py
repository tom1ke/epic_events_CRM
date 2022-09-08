from django.db import models


class Status(models.Model):
    contract = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE, related_name='active')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='active')
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Active' if self.active is True else 'Passed'