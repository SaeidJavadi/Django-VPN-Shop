from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class vpnlist(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("VPN Title"))
    day = models.IntegerField(verbose_name=_("Active Day"))
    price_t = models.CharField(max_length=150, verbose_name=_("Price Toman"))
    price_c = models.CharField(max_length=150, verbose_name=_("Price Digital currency"), blank=True, null=True)
    row = models.IntegerField(verbose_name=_("Row"))
    color = models.CharField(max_length=150, verbose_name=_("Color"), null=True, blank=True)

    class Meta:
        verbose_name = _("vpnlist")
        verbose_name_plural = _("vpnlists")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vpnlist_detail", kwargs={"pk": self.pk})


class Sidebar(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("title"))
    content = RichTextField(verbose_name=_("content"))

    class Meta:
        verbose_name = _('Sidebar')
        verbose_name_plural = _('Sidebars')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sidebar_detail", kwargs={"pk": self.pk})
