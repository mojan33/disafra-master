from django.contrib import admin
from core.producto.models import Producto,Marca,DetalleProducto


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['id_marca','marca']
    list_filter = ['marca']
    list_editable = ['marca']
    list_per_page = 10
    search_fields = ['marca']


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['cod_producto','nombre','porcentaje_ganancia','precio_venta','cantidad','sucursal']
    list_filter = ['recien_ingreso','marca','fecha_vencimiento']
    list_editable = ['nombre','porcentaje_ganancia','precio_venta','sucursal']
    list_per_page = 10
    search_fields = ['nombre','marca','sucursal','precio_venta','categoria']


class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ['id_detalle_producto','proveedor','producto_cod','precio_costo']
    list_filter = ['proveedor','producto_cod']
    list_editable = ['proveedor','precio_costo']
    list_per_page = 10
    search_fields = ['producto_cod','proveedor']


admin.site.register(Marca,MarcaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(DetalleProducto,DetalleProductoAdmin)