from django.shortcuts import render,  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from vpn.froms import vpnlistForm
from vpn.models import vpnlist


def home(request):
    vpli = vpnlist.objects.all().order_by('row')
    return render(request=request, template_name="vpn/home.html", context={'vpnall': vpli})


def vpnbuy(request):
    vpli = vpnlist.objects.all().order_by('row')
    return render(request=request, template_name="vpn/buy.html", context={'vpnall': vpli})
