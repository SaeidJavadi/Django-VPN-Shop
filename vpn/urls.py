from django.urls import path
from vpn.views import home

app_name = 'vpn'

urlpatterns = [
    path('', home, name='home'),
]
