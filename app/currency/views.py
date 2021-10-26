from currency.models import ContactUs, Rate

from django.shortcuts import render


def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'contact_us.html', context)


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)
