import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data: dict = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords should match!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.username = str(uuid.uuid4())
        user.save()
        self._send_email()
        return user

    def _send_email(self):
        subject = 'Thanks for sign up'
        path = reverse('account:activate', args=(self.instance.username,))
        body = f'''
        {settings.HTTP_SCHEMA}://{settings.DOMAIN}{path}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False,
        )


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'your class',
        'placeholder': 'your placeholder',
        'type': 'email',
        'name': 'email'
    }))


class PasswordChangingForm(PasswordChangeForm):
    current_password = forms.CharField(max_length=100,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    confirm_new_password = forms.CharField(max_length=100,
                                           widget=forms.PasswordInput(
                                               attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('current_password', 'new_password', 'confirm_new_password')
