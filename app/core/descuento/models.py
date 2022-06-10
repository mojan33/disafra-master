from django.db import models


class Descuento(models.Model):
    cod_descuento = models.CharField(db_column='COD_DESCUENTO', primary_key=True, max_length=25)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='PORCENTAJE', max_digits=4, decimal_places=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.cod_descuento} - {self.porcentaje}%'

    class Meta:
        managed = False
        db_table = 'descuento'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'