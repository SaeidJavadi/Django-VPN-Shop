from django.urls import path
from vpn.views import home, vpnbuy, buyVerify, HelpListView, HelpDetailView

app_name = 'vpn'
urlpatterns = [
    path('', home, name='home'),
    path('buy', vpnbuy, name='buy'),
    path('buyVerify', buyVerify, name='buyVerify'),
    path('helplist', HelpListView.as_view(), name='helplist'),
    path('help/<int:pk>/', HelpDetailView.as_view(), name='help'),
]
