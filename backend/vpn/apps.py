from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VpnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vpn'
    verbose_name = _('VPN')
