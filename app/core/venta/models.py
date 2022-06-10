from django.db import models
from core.cliente.models import Cliente
from core.empleado.models import Empleado
from core.sucursal .models import Sucursal
from core.producto.models import Producto
from core.descuento.models import Descuento


class Venta(models.Model):
    num_venta = models.IntegerField(db_column='NUM_VENTA', primary_key=True)  # Field name made lowercase.
    cliente_nit = models.ForeignKey(Cliente, on_delete=models.SET_NULL, db_column='CLIENTE_NIT', blank=True, null=True)  # Field name made lowercase.
    empleado_cod = models.ForeignKey(Empleado, on_delete=models.SET_NULL, db_column='EMPLEADO_COD', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, db_column='SUCURSAL_ID', blank=True, null=True)  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='FECHA_VENTA')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(db_column='ID_DETALLE_VENTA', primary_key=True)  # Field name made lowercase.
    producto_cod = models.ForeignKey(Producto, on_delete=models.SET_NULL, db_column='PRODUCTO_COD', blank=True, null=True)  # Field name made lowercase.
    venta_num = models.ForeignKey(Venta, on_delete=models.SET_NULL, db_column='VENTA_NUM', blank=True, null=True)  # Field name made lowercase.
    descuento_cod = models.ForeignKey(Descuento, on_delete=models.SET_NULL, db_column='DESCUENTO_COD', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'