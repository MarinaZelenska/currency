from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'created',
            'source',
            'type',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'logo',
            'code_name',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )

    def create(self, validate_data):
        instance = super(ContactUsSerializer, self).create(validate_data)
        send_mail(
            'Subject: {}'.format(instance.subject),
            'Body: {}'.format(instance.message),
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
        )
        return instance
