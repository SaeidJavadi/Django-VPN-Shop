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


class Conf(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    sidebar = RichTextField(verbose_name=_("Sidebar"))
    headtext1 = models.TextField(verbose_name=_("Head Text 1"), null=True, blank=True)
    headtext2 = models.TextField(verbose_name=_("Head Text 2"), null=True, blank=True)
    logo = models.ImageField(upload_to="logo", null=True, blank=True, verbose_name=_("Site Logo"))
    buynote = models.TextField(verbose_name=_("Buy Note"),null=True, blank=True)

    class Meta:
        verbose_name = _("Site Config")
        verbose_name_plural = _("Site Configs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("conf_detail", kwargs={"pk": self.pk})


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


class Help(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    content = RichTextField(verbose_name=_("Content"))
    image = models.ImageField(upload_to="help", verbose_name=_("Image"), null=True, blank=True)
    file = models.FileField(upload_to="dl", max_length=100, null=True, blank=True, verbose_name=_("File"))

    class Meta:
        verbose_name = _("Help")
        verbose_name_plural = _("Helps")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Help_detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.IntegerField(verbose_name=_('Phone Number'), null=True, blank=True)
    message = models.TextField(verbose_name=_('Message'))
    status = models.CharField(max_length=60, verbose_name=_('Status'),
                              choices=(('Read', _('Read')), ('UnRead', _('UnRead'))), default='UnRead')

    class Meta:
        verbose_name = _('Contact us')
        verbose_name_plural = _('Contact us')

    def __str__(self):
        return self.email
