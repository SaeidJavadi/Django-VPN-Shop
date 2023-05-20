from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm, EditProfileForm
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


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
    form_password = ResetPassword(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _('updated successfully.'), extra_tags='alert alert-success')
            return redirect('accounts:profile')
        elif form_password.is_valid():
            cd = form_password.cleaned_data
            user.set_password(cd['password1'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password has been successfully changed'), 'success')
            logout(request)
            return redirect('accounts:login')
        else:
            # cd = form.cleaned_data
            # error = ''
            # if User.objects.filter(email=cd['email']).exists():
            #     error = 'ایمیلی که وارد کرده اید از قبل وجود دارد'
            # if User.objects.filter(email=cd['phone']).exists():
            #     error = 'شماره تلفنی که وارد کرده اید از قبل وجود دارد!!'
            # elif User.objects.filter(idcode=cd['idcode']).exists():
            #     error = 'کدملی که وارد کرده اید از قبل وجود دارد!!'
            messages.success(request, _('Error updating your profile!!'), extra_tags='warning')
            return redirect('accounts:profile')
    else:
        return render(request, 'accounts/profile.html', {'user':user, 'form': form, 'form_password':form_password})
