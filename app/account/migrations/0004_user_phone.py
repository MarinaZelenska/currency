# Generated by Django 3.2.7 on 2021-12-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=34, null=True),
        ),
    ]
