from django.contrib import admin
from core.descuento.models import Descuento


class DescuentoAdmin(admin.ModelAdmin):
    list_display = ['cod_descuento','porcentaje','descripcion']
    list_filter = ['porcentaje']
    list_editable = ['porcentaje','descripcion']
    list_per_page = 10
    search_fields = ['descripcion']


admin.site.register(Descuento,DescuentoAdmin)