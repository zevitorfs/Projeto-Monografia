from django.contrib import admin
from . import models


class produtoadimin(admin.ModelAdmin):
    list_display = ['nome', 'publicacao']


admin.site.register(models.anexar_arquivo, produtoadimin)
