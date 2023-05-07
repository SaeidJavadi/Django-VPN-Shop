from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class vpnbuy(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("VPN Name"))
    day = models.IntegerField(verbose_name=_("Active Day"))
    price_t = models.CharField(max_length=150, verbose_name=_("Price Toman"))
    price_c = models.CharField(max_length=150, verbose_name=_("Price Digital currency"))
    vpnrow = models.IntegerField(verbose_name=_("Row"))
    color = models.CharField(max_length=150, verbose_name=_(
        "Color"), null=True, blank=True)

    class Meta:
        verbose_name = _("vpnbuy")
        verbose_name_plural = _("vpnbuys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vpnbuy_detail", kwargs={"pk": self.pk})
