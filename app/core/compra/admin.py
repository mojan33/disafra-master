from django.contrib import admin
from core.compra.models import Compra,DetalleCompra
from core.pago.models import PagoCompra


class PagoCompraInline(admin.TabularInline):
    model = PagoCompra


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra


class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraInline,PagoCompraInline]
    list_display = ['num_compra','descripcion','total','total_pagado','pagado','fecha_compra','entregado','fecha_entregado','visitador','empleado_cod']
    list_filter = ['pagado','entregado','fecha_entregado','fecha_compra','visitador','empleado_cod']
    list_editable = ['pagado','entregado','fecha_entregado']
    list_per_page = 10
    search_fields = ['num_compra']


class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ['id_detalle_compra', 'detalle_producto', 'cantidad', 'subtotal', 'compra_num']
    list_filter = ['compra_num']
    list_editable = ['cantidad']
    list_per_page = 10
    search_fields = ['id_compra', 'detalle_producto', 'compra_num']


admin.site.register(Compra,CompraAdmin)
admin.site.register(DetalleCompra,DetalleCompraAdmin)