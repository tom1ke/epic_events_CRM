from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

class Client(models.Model):
    sales_contact = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_regex], max_length=16)
    mobile = models.CharField(validators=[phone_regex], max_length=16)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField
    