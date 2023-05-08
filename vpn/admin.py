from django.contrib import admin
from vpn.models import vpnlist


@admin.register(vpnlist)
class vpnlistAdmin(admin.ModelAdmin):
    list_display = ("title", "color", "row", "price_c", "price_t", "day")
    list_editable = ("row", "day")
    list_display_links = ("title",)
    search_fields = ("title", "day")
    list_filter = ("row", "day", "price_t")
