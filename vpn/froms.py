from django import forms
from django.utils.translation import gettext_lazy as _
from vpn.models import vpnlist


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
