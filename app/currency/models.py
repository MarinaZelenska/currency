from currency import model_choices as mch

from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(  # noqa: A003
        choices=mch.RateTypeChoices.choices,
        default=mch.RateTypeChoices.USD,
    )
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=250)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
