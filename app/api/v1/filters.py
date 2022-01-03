from currency.models import ContactUs, Rate

import django_filters


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ['gte', 'lte', 'exact'],
            'sale': ['gte', 'lte', 'exact'],
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'email_from',
        }
