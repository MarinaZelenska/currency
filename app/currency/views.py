from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.tasks import send_email_in_background

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


# ContactUS
class ContactListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contact_list')
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        subject = 'User ContactUs'
        body = f'''
            Email to reply: {self.object.email_from}
            Subject: {self.object.subject}
            Body: {self.object.message}
        '''
        send_email_in_background.delay(subject, body)
        # send_email_in_background.apply_async(args=(subject, body))
        '''
        00-8.59 | 9.00-19.00 | 19.01 - 23.59
        9.00    |    send    | 9.00 next day
        '''
        # from datetime import datetime, timedelta
        # eta = datetime(2021, 11, 21, 19, 00, 00)
        # send_email_in_background.apply_async(
        #     kwargs={'subject': subject, 'body': body},
        #     countdown=120,
        # eta=eta,
        # )
        return redirect


# Rate
class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailsView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


# Source
class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source_list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')
