from django.contrib import admin
from .models import Ment

class MentAdmin(admin.ModelAdmin):
    list_display = ("hostname", "mac", "ip", "sn")
    search_fields = ("hostname"," mac")
    list_filter = ("hostname", "mac")


admin.site.register(Ment, MentAdmin)

# Register your models here.
