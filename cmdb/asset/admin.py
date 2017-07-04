from django.contrib import admin
from . import models


class AssetAdmin(admin.ModelAdmin):
    list_display = ("username", "mac")
    search_fields = ("username", "mac")
    list_filter = ("username", "mac")
admin.site.register(models.Asset, AssetAdmin)
