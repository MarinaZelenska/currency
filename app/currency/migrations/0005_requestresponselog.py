# Generated by Django 3.2.7 on 2021-11-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_alter_rate_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('request_method', models.CharField(max_length=10)),
                ('time', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
