from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from accounts.models import User


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
    headtext1 = models.TextField(verbose_name=_("Head Text 1"), null=True, blank=True)
    headtext2 = models.TextField(verbose_name=_("Head Text 2"), null=True, blank=True)
    logo = models.ImageField(upload_to="logo", null=True, blank=True, verbose_name=_("Site Logo"))

    class Meta:
        verbose_name = _("Sidebar")
        verbose_name_plural = _("Sidebars")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sidebar_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_("User"), null=True, blank=True)
    vpn = models.ForeignKey(vpnlist, on_delete=models.SET_NULL, verbose_name=_("VPN"), null=True, blank=True)
    buydate = models.DateTimeField(auto_now_add=True, verbose_name=_("Buy Date"))
    status = models.BooleanField(verbose_name=_("Status"))
    refid = models.CharField(max_length=200, verbose_name=_("Ref ID"))
    authority = models.CharField(max_length=200, verbose_name=_("Authority"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
