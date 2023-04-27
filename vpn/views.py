from django.shortcuts import render,  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request=request, template_name="vpn/home.html", context={})
