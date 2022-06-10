from django.contrib import admin
from core.venta.models import Venta,DetalleVenta


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta


class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]
    list_display = ['num_venta','cliente_nit','empleado_cod','sucursal','fecha_venta','total']
    list_filter = ['empleado_cod','sucursal','fecha_venta']
    list_editable = ['cliente_nit']
    list_per_page = 10
    search_fields = ['cliente_nit','empleado_cod','sucursal']


class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['id_detalle_venta','producto_cod','venta_num','descuento_cod','cantidad','subtotal']
    list_filter = []
    list_editable = ['producto_cod','cantidad','descuento_cod']
    list_per_page = 10
    search_fields = ['producto_cod','venta_num','descuento_cod']


admin.site.register(Venta,VentaAdmin)
admin.site.register(DetalleVenta,DetalleVentaAdmin)