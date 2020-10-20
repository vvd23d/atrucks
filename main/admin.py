from django.contrib import admin

from .models import Numbering


class NumberingAdmin(admin.ModelAdmin):
    list_display = ("kod", "fr", "to", "capacity", "operator", "region")
    list_filter = ('operator', 'region')


admin.site.register(Numbering, NumberingAdmin)

