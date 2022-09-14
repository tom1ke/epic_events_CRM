from django.db import models


class Status(models.Model):
    
    class Meta:
        verbose_name_plural = 'status'
    
    
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label