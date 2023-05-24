from django.contrib import admin
from vpn.models import vpnlist, Conf, Order, Help, Contact


@admin.register(vpnlist)
class vpnlistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "color", "row", "price_c", "price_t", "day")
    list_editable = ("row", "day")
    list_display_links = ("title",)
    search_fields = ("title", "day")
    list_filter = ("row", "day", "price_t")


@admin.register(Conf)
class ConfAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "vpn", "authority", "refid", "status", "buydate")
    search_fields = ("user", "vpn", "authority", "refid")
    list_filter = ("vpn", "status", "buydate")


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ("content", "title")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( "status", "phone", "email", "name")
    list_editable = ("status",)
