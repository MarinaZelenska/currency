# Generated by Django 3.2.7 on 2021-11-24 15:26

import currency.models

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_rate_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=None, null=True, upload_to=currency.models.logo_upload_to),
        ),
    ]
