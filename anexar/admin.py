from django.contrib import admin
from . import models


class arquivoadimin(admin.ModelAdmin):
    list_display = ['nome', 'publicacao']


admin.site.register(models.anexar, arquivoadimin)
