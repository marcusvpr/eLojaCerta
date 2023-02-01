from django.contrib import admin
from . import models


class TabelaIntAdmin(admin.ModelAdmin):
    list_display = ('id', 'tabela', 'codigo', 'descricao')
    list_display_links = ('id', 'tabela', 'codigo')


admin.site.register(models.TabelaInt, TabelaIntAdmin)
