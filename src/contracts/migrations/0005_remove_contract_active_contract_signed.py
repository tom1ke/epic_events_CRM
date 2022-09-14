# Generated by Django 4.1 on 2022-09-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_remove_contract_status_contract_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='active',
        ),
        migrations.AddField(
            model_name='contract',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]