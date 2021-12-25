from api.v1.pagination import RatePagination

from currency.models import ContactUs, Rate, Source

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import generics
from rest_framework import viewsets

from .filters import ContactUsFilter, RateFilter
from .serializer import ContactUsSerializer, RateSerializer, SourceSerializer
from .throttles import AnonCurrencyThrottle


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json.loads, json.dumps
    pagination_class = RatePagination
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonCurrencyThrottle]


class SourceApiView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
    filterset_class = ContactUsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['email_from', 'subject', 'message']
    search_fields = ['email_from', 'subject']
