from currency.models import Rate

import django_filters


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
        )
