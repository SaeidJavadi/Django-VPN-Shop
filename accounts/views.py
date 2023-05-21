from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm, EditProfileForm, ChangePassword
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def userRegister(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not User.objects.filter(email=cd['email']).exists():
                user = User.objects.create_user(phone=cd['phone'], email=cd['email'], password=cd['password1'])
                user.save()
                messages.success(request, _("You successfully registered a user"), extra_tags="success")
                return redirect('vpn:home')
            else:
                messages.error(request, _("This Email is exists"), extra_tags="warning")
        else:
            import json
            er = json.loads(form.errors.as_json())
            for e in er:
                messages.error(request, er[e][0]['message'], 'warning')
    return render(request, 'accounts/register.html', {'form': form})


def userLogin(request):
    if not request.user.is_active:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if User.objects.filter(email=cd['email']).exists():
                    user = authenticate(request, email=cd['email'], password=cd['password'])
                    if user is not None:
                        login(request, user)
                        messages.success(request, _("logged in successfully"), extra_tags="success")
                        return redirect('vpn:buy')
                    else:
                        messages.error(request, _("your email Or Password is wrong"), extra_tags="warning")
                else:
                    messages.error(request, _("No account created with this email"), extra_tags="warning")
                    return redirect('accounts:login')
            else:
                messages.error(request, _("Please enter your information correctly"), extra_tags="warning")
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('vpn:home')


@login_required()
def LogoutPage(request):
    logout(request)
    messages.success(request, _("You Logged Out successfully"), extra_tags="success")
    return redirect('vpn:home')


@login_required()
def profile(request):
    user = User.objects.get(email=request.user.email)
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _("updated successfully"), extra_tags="alert alert-success")
            return redirect('accounts:profile')
        else:
            messages.success(request, _("Error updating your profile !!"), extra_tags="warning")
            return redirect('accounts:profile')
    else:
        request.session['email'] = user.email
        return render(request, 'accounts/profile.html', {'form': form})


def resetpass(request):
    if request.user.is_active:
        if request.method == 'POST':
            form = ChangePassword(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(email=request.session['email'])
                user.set_password(cd['password1'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, _("Your password has been successfully changed"), extra_tags="success")
                return redirect('accounts:login')
        else:
            if request.session['email']:
                form = ChangePassword()
                return render(request, 'accounts/reset.html', {'form': form})
    else:
        return redirect('vpn:home')
