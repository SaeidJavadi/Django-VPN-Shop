from django.urls import path
from vpn.views import home, vpnbuy, buyVerify, HelpListView, HelpDetailView, contact, dashboard

app_name = 'vpn'
urlpatterns = [
    path('', home, name='home'),
    path('buy', vpnbuy, name='buy'),
    path('buyVerify', buyVerify, name='buyVerify'),
    path('helplist', HelpListView.as_view(), name='helplist'),
    path('help/<int:pk>/', HelpDetailView.as_view(), name='help'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
]
