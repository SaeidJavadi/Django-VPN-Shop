from django.shortcuts import render, redirect
from django.conf import settings
import requests
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from vpn.models import vpnlist, Order
from accounts.models import User

# sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = settings.SITE_ADDRESS  # Required
# Important: need to edit for realy server.
CallbackURL = f'{settings.SITE_ADDRESS}/payment/verify/'
phone = None         # Optional
email = None         # Optional
order_id = None      # Optional


@login_required()
def send_request(request, vid):
    print("="*30)
    print(vid, request.user.email)
    print("="*30)
    vpn = vpnlist.objects.get(id=vid)
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": vpn.price_t,
        "Description": description,
        "CallbackURL": CallbackURL,
        "Phone": phone,
        "email": request.user.email,
        "order_id": order_id
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                dt = {'status': True, 'url': ZP_API_STARTPAY +
                      str(response['Authority']), 'authority': response['Authority']}
                print("="*30)
                print(dt)
                print("="*30)
                return redirect(f"{ZP_API_STARTPAY}{str(response['Authority'])}")
            else:
                return {'status': False, 'code': str(response['Status'])}
        return HttpResponse(response)
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": request.GET['Authority']
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return HttpResponse(str({'status': True, 'RefID': response['RefID']}))
        else:
            return HttpResponse(str({'status': False, 'code': str(response['Status'])}))
    return response
