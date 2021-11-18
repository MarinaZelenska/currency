from currency.models import Rate, Source

from django import forms
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'type',
            'source',

        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
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
