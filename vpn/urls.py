from django.urls import path
from vpn.views import home, vpnbuy

app_name = 'vpn'
urlpatterns = [
    path('', home, name='home'),
    path('buy', vpnbuy, name='buy'),
]
