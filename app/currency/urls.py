

from currency.views import (
    ContactListView,
    RateCreateView, RateDeleteView, RateDetailsView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceListView, SourceUpdateView
)

from django.urls import path
app_name = 'currency'

urlpatterns = [

    path('contact-us/', ContactListView.as_view(), name='contact_list'),

    path('rate/list/', RateListView.as_view(), name='rate_list'),
    path('rate/create/', RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate_update'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate_details'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate_delete'),

    path('source/list/', SourceListView.as_view(), name='source_list'),
    path('source/create/', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),


]
