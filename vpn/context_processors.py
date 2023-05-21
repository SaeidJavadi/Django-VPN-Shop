from django.conf import settings
from vpn.models import Sidebar


def siteAddress(request):
    return {'SITE_ADDRESS': settings.SITE_ADDRESS}


def sideBar(request):
    sidbar = Sidebar.objects.last()
    return {'SIDEBAR': sidbar}
