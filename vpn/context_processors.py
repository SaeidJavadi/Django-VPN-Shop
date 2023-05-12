from django.conf import settings


def siteAddress(request):
    return {'SITE_ADDRESS': settings.SITE_ADDRESS}
