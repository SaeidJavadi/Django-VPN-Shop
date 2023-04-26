from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.decorators import login_required


@login_required()
def userRegister(request):
    if request.user.is_active:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if not User.objects.filter(username=cd['username']).exists():
                    if not User.objects.filter(email=cd['email']).exists():
                        user = User.objects.create_user(
                            username=cd['username'], email=cd['email'], password=cd['password1'])
                        user.save()
                        messages.success(request, 'You successfully registered a user', 'success')
                        return redirect('creator:index')
                    else:
                        messages.error(request, 'This Email is exists',
                                       'warning')
                else:
                    messages.error(request, 'This Username is exists', 'warning')
            else:
                import json
                _ = json.loads(form.errors.as_json())
                for e in _:
                    messages.error(request, _[e][0]['message'], 'warning')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect('creator:index')


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
                        messages.success(request, 'logged in successfully', 'success')
                        return redirect('creator:index')
                    else:
                        messages.error(request, 'your username Or Password is wrong', 'warning')
                else:
                    messages.error(request, 'No account created with this username',
                                   'warning')
                    return redirect('accounts:login')
            else:
                messages.error(request, 'Please enter your information correctly', 'warning')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('creator:index')


def LogoutPage(request):
    logout(request)
    messages.success(request, 'You Logged Out successfully', 'success')
    return redirect('creator:index')
