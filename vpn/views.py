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
        vpnid = request.POST.get('vvpnid')
        return redirect('payment:pay', vid=vpnid)
    else:
        vpli = vpnlist.objects.all().order_by('row')
        return render(request=request, template_name="vpn/buy.html", context={'vpnall': vpli})


def buyVerify(request):
    v = vpnlist.objects.get(id=request.POST.get('vpnid'))
    return render(request=request, template_name="vpn/verify.html", context={'vpn': v})
