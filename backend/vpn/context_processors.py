from django.conf import settings
from vpn.models import Conf


def siteAddress(request):
    return {'SITE_ADDRESS': settings.SITE_ADDRESS}


def sideBar(request):
    conf = Conf.objects.last()
    return {'SITECONF': conf}
