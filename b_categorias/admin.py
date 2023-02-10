from django.contrib import admin
from .models import B_Categoria


class B_CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_links = ('id', 'nome_cat')


admin.site.register(B_Categoria, B_CategoriaAdmin)
