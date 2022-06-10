from django.contrib import admin
from core.cotizacion.models import Cotizacion,DetalleCotizacion


class DetalleCotizacionInline(admin.TabularInline):
    model = DetalleCotizacion


class CotizacionAdmin(admin.ModelAdmin):
    inlines = [DetalleCotizacionInline]
    list_display = ['num_cotizacion','cliente_nit','empleado_cod','sucursal','fecha_venta','total']
    list_filter = ['cliente_nit','sucursal','empleado_cod','fecha_venta']
    list_editable = ['cliente_nit']
    list_per_page = 10
    search_fields = ['cliente_nit','sucursal']


class DetalleCotizacionAdmin(admin.ModelAdmin):
    list_display = ['id_detalle_cotizacion','producto_cod','cotizacion_num','descuento_cod','cantidad','subtotal']
    list_filter = ['producto_cod','descuento_cod']
    list_editable = ['producto_cod','descuento_cod','cantidad']
    list_per_page = 10
    search_fields = ['producto_cod','descuento_cod','cotizacion_num']


admin.site.register(Cotizacion,CotizacionAdmin)
admin.site.register(DetalleCotizacion,DetalleCotizacionAdmin)