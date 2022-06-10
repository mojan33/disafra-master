from django.db import models


class TipoTelefono(models.Model):
    id_tipo_telefono = models.IntegerField(db_column='ID_TIPO_TELEFONO', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_telefono'
        verbose_name = 'Tipo de Teléfono'
        verbose_name_plural = 'Tipos de Teléfonos'


class Telefono(models.Model):
    num_telefono = models.CharField(db_column='NUM_TELEFONO', primary_key=True, max_length=16)  # Field name made lowercase.
    tipo_telefono = models.ForeignKey(TipoTelefono, models.DO_NOTHING, db_column='TIPO_TELEFONO_ID', blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='EXTENSION', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefono'
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'