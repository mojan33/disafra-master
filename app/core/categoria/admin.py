from django.contrib import admin
from core.categoria.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria','nombre','descripcion']
    list_filter = ['categoria_sub']
    list_editable = ['nombre','descripcion']
    list_per_page = 10
    search_fields = ['nombre','categoria_sub']


admin.site.register(Categoria,CategoriaAdmin)