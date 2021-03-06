from currency import model_choices as mch

from django.db import models
from django.templatetags.static import static


def logo_upload_to(instance, filename):
    return f'logo/{instance.id}/{filename}'


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(  # noqa: A003
        choices=mch.RateTypeChoices.choices,
        default=mch.RateTypeChoices.USD,
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=250)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    logo = models.FileField(
        upload_to=logo_upload_to,
        default=None,
        null=True,
        blank=True,
    )
    code_name = models.CharField(max_length=64, unique=True)

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return static('images/default-logo.png')

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=10)
    time = models.DecimalField(max_digits=6, decimal_places=2)
