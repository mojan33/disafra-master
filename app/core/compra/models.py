from django.db import models
from core.proveedor.models import Visitador
from core.empleado.models import Empleado
from core.producto.models import DetalleProducto


class Compra(models.Model):
    num_compra = models.IntegerField(db_column='NUM_COMPRA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.
    total_pagado = models.DecimalField(db_column='TOTAL_PAGADO', max_digits=7, decimal_places=2)  # Field name made lowercase.
    pagado = models.IntegerField(db_column='PAGADO')  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='FECHA_COMPRA')  # Field name made lowercase.
    entregado = models.IntegerField(db_column='ENTREGADO')  # Field name made lowercase.
    fecha_entregado = models.DateField(db_column='FECHA_ENTREGADO')  # Field name made lowercase.
    visitador = models.ForeignKey(Visitador, models.DO_NOTHING, db_column='VISITADOR_ID', blank=True, null=True)  # Field name made lowercase.
    empleado_cod = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='EMPLEADO_COD', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.num_compra} - {self.total} - {self.fecha_compra}'

    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(models.Model):
    id_detalle_compra = models.IntegerField(db_column='ID_DETALLE_COMPRA', primary_key=True)  # Field name made lowercase.
    detalle_producto = models.ForeignKey(DetalleProducto, models.DO_NOTHING, db_column='DETALLE_PRODUCTO_ID', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.
    compra_num = models.ForeignKey(Compra, models.DO_NOTHING, db_column='COMPRA_NUM', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.id_detalle_compra} - {self.cantidad} - {self.subtotal} - {self.compra_num.num_compra}'

    class Meta:
        managed = False
        db_table = 'detalle_compra'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compras'