from django.contrib import admin
from core.pago.models import PagoCompra


class PagoCompraAdmin(admin.ModelAdmin):
    list_display = ['num_pago','descripcion','fecha_pago','cantidad_pagada','empleado_cod','compra_num']
    list_filter = ['fecha_pago']
    list_editable = ['descripcion','cantidad_pagada']
    list_per_page = 10
    search_fields = ['empleado_cod','descripcion']


admin.site.register(PagoCompra,PagoCompraAdmin)