from currency.models import ContactUs

from django.http.response import HttpResponse


def contact_us(request):
    contact = ContactUs.objects.all()
    result = []
    for item in contact:
        result.append(f'ID:{item.id},'
                      f'Email:{item.email_from},'
                      f'Subject:{item.subject},'
                      f'Message:{item.message}<br>')
    return HttpResponse(str(result))


def hello_world(request):
    return HttpResponse('Hello World')
