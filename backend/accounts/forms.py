from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', 'email', 'is_active', 'is_staff')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'email', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),   # 'placeholder': 'Email'
        label='Email')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'dir': 'ltr'}),  # 'placeholder': 'Password'
        label='Password')


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'dir': 'ltr', 'onChange': 'onChange()'}))
    #    ,'minlength': '8'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'dir': 'ltr', 'onChange': 'onChange()'}))

    class Meta:
        model = User
        fields = ('phone', 'email')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)', 'required': 'false'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        else:
            return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone',)
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'dir': 'ltr', 'readonly': 'true'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)', 'required': 'false'}),
        }


class ChangePassword(forms.Form):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'dir': 'ltr', 'onChange': 'onChange()'}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Re-Enter Password',
                                           'dir': 'ltr', 'onChange': 'onChange()'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        else:
            return password2
