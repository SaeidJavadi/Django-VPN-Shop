from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm, EditProfileForm, ChangePassword
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import update_session_auth_hash


def userRegister(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not User.objects.filter(username=cd['username']).exists():
                if not User.objects.filter(phone=cd['phone']).exists():
                    if not User.objects.filter(email=cd['email']).exists():
                        user = User.objects.create_user(
                            username=cd['username'], phone=cd['phone'], email=cd['email'], password=cd['password1'])
                        user.save()
                        messages.success(request, _('You successfully registered a user'), 'success')
                        return redirect('vpn:home')
                    else:
                        messages.error(request, _('This Email is exists'), 'warning')
                else:
                    messages.error(request, _('This Username is exists'), 'warning')
            else:
                messages.error(request, _('This Username is exists'), 'warning')
        else:
            import json
            _ = json.loads(form.errors.as_json())
            for e in _:
                messages.error(request, _[e][0]['message'], 'warning')
    return render(request, 'accounts/register.html', {'form': form})


def userLogin(request):
    if not request.user.is_active:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if User.objects.filter(username=cd['username']).exists():
                    user = authenticate(request, username=cd['username'], password=cd['password'])
                    if user is not None:
                        login(request, user)
                        messages.success(request, _('logged in successfully'), 'success')
                        return redirect('vpn:home')
                    else:
                        messages.error(request, _('your username Or Password is wrong'), 'warning')
                else:
                    messages.error(request, _('No account created with this username'), 'warning')
                    return redirect('accounts:login')
            else:
                messages.error(request, _('Please enter your information correctly'), 'warning')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('vpn:home')


@login_required()
def LogoutPage(request):
    logout(request)
    messages.success(request, _('You Logged Out successfully'), 'success')
    return redirect('vpn:home')


@login_required()
def profile(request):
    user = User.objects.get(email=request.user.email)
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _('updated successfully'), extra_tags='alert alert-success')
            return redirect('accounts:profile')
        else:
            messages.success(request, _('Error updating your profile !!'), extra_tags='warning')
            return redirect('accounts:profile')
    else:
        request.session['email'] = user.email
        request.session['username'] = user.username
        print(user.email, user.username)
        return render(request, 'accounts/profile.html', {'form': form})


def resetpass(request):
    if request.user.is_active:
        if request.method == 'POST':
            form = ChangePassword(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(email=request.session['email'], username=request.session['username'])
                user.set_password(cd['password1'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, _('Your password has been successfully changed'), 'success')
                return redirect('accounts:login')
        else:
            if request.session['email'] and request.session['username']:
                form = ChangePassword()
                return render(request, 'accounts/reset.html', {'form': form})
    else:
        return redirect('vpn:home')
