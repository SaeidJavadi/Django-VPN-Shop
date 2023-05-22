from django.shortcuts import render,  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from vpn.models import vpnlist
from django.http import HttpResponse


def home(request):
    vpli = vpnlist.objects.all().order_by('row')
    return render(request=request, template_name="vpn/home.html", context={'vpnall': vpli})


def vpnbuy(request):
    if request.method == "POST":
        vpnid = request.POST.get('vpnid')
        v = vpnlist.objects.get(id=vpnid)
        return HttpResponse(str(v.title + "-"+v.price_t+"-"+f'{v.day}'+"-"+f'{v.id}'))
    else:
        vpli = vpnlist.objects.all().order_by('row')
        return render(request=request, template_name="vpn/buy.html", context={'vpnall': vpli})
