from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.core.mail import send_mail
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

    def _send_email(self):
        subject = 'User ContactUs'
        body = f'''
               Email to reply: {self.object.email_from}
               Subject: {self.object.subject}
               Body: {self.object.message}
           '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


# Rate
class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'rate_update.html'


class RateDetailsView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


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
