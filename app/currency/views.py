from django.shortcuts import render
from django.http.response import HttpResponse

from currency.models import ContactUs


def hello_world(request):
    return HttpResponse('Hello World')


def contact_us(request):
    contact = ContactUs.objects.all()
    result = []
    for item in contact:
        result.append(f'ID: {item.id}, Email: {item.email_from}, Subject: {item.subject}, Message: {item.message} <br>')
    return HttpResponse(str(result))
