# Generated by Django 4.1 on 2022-09-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
