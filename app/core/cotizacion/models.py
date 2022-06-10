from django.db import models
from core.cliente.models import Cliente
from core.empleado.models import Empleado
from core.sucursal.models import Sucursal
from core.producto.models import Producto
from core.descuento.models import Descuento


class Cotizacion(models.Model):
    num_cotizacion = models.IntegerField(db_column='NUM_COTIZACION', primary_key=True)  # Field name made lowercase.
    cliente_nit = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_NIT', blank=True, null=True)  # Field name made lowercase.
    empleado_cod = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='EMPLEADO_COD', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='SUCURSAL_ID', blank=True, null=True)  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='FECHA_VENTA')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return f'{self.num_cotizacion} - {self.sucursal} - {self.total}'

    class Meta:
        managed = False
        db_table = 'cotizacion'
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'


class DetalleCotizacion(models.Model):
    id_detalle_cotizacion = models.IntegerField(db_column='ID_DETALLE_COTIZACION', primary_key=True)  # Field name made lowercase.
    producto_cod = models.ForeignKey(Producto, models.DO_NOTHING, db_column='PRODUCTO_COD', blank=True, null=True)  # Field name made lowercase.
    cotizacion_num = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='COTIZACION_NUM', blank=True, null=True)  # Field name made lowercase.
    descuento_cod = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='DESCUENTO_COD', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return f'{self.id_detalle_cotizacion} - {self.cantidad} - {self.subtotal}'

    class Meta:
        managed = False
        db_table = 'detalle_cotizacion'
        verbose_name = 'Detalle de Cotización'
        verbose_name_plural = 'Detalles de Cotizaciones'
