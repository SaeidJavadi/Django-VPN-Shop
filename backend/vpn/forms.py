from django import forms
from django.utils.translation import gettext_lazy as _
from vpn.models import vpnlist, Contact


class vpnlistForm(forms.ModelForm):
    class Meta:
        model = vpnlist
        fields = ('title', 'day', 'price_t', 'price_c', 'row', 'color')
        widgets = {
            'title': forms.RadioSelect(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'title',
        }
        forceInputField = 'This field is required'
        error_messages = {
            'title': {
                'required': forceInputField,
            },
            'day': {
                'required': forceInputField,
            },
            'price_t': {
                'required': forceInputField,
            }
        }
        help_texts = {
            'title': 'First select your vpn',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'data-error': 'Enter your name', 'placeholder': 'Your Name',
                       'style': 'color:#00FF3E;text-align: center;background-color:#2e2e2ea4;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'Enter your email',
                                             'placeholder': 'your email', 'style': 'color:#00FF3E;text-align: center;background-color:#2e2e2ea4;'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Enter your phone number',
                                              'placeholder': 'Your phone number', 'maxlength': '11', 'dir': 'ltr',
                                              'minlength': '11', 'type': 'tel', 'style': 'color:#00FF3E;text-align: center;background-color:#2e2e2ea4;', 'onkeypress': 'return isNumber(event)', 'required': 'false'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'data-error': 'Write your message', 'placeholder': 'Your Message',
                       'style': 'color:#00FF3E;background-color:#2e2e2ea4;'})
        }
