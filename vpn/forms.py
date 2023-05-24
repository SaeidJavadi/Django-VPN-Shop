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
            'title': 'عنوان',

        }
        forceInputField = 'این فیلد اجباری است'
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
            'title': 'ابتدا نوع وی پی ان خود را انتخاب کنید',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'data-error': 'لطفا نام خود را وارد کنید', 'placeholder': 'نام شما',
                       'style': 'color:#00FF3E'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'لطفا ایمیل خود را وارد کنید',
                                             'placeholder': 'ایمیل شما', 'style': 'color:#00FF3E'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'لطفا شماره خود را وارد کنید',
                                              'placeholder': 'شماره تماس شما', 'maxlength': '11', 'dir': 'ltr',
                                              'minlength': '11', 'type': 'tel', 'style': 'color:#00FF3E'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'data-error': 'پیام خود را بنویسید', 'placeholder': 'پیام شما',
                       'style': 'color:#00FF3E'})
        }
