from django.db import models
from core.direccion.models import Direccion
from core.telefono.models import Telefono


class Sucursal(models.Model):
    id_sucursal = models.IntegerField(db_column='ID_SUCURSAL', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100)  # Field name made lowercase.
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='DIRECCION_ID', blank=True, null=True)  # Field name made lowercase.
    telefono_num = models.ForeignKey(Telefono, models.DO_NOTHING, db_column='TELEFONO_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'


class UsuarioSucursal(models.Model):
    usuario_sucursal = models.CharField(db_column='USUARIO_SUCURSAL', primary_key=True, max_length=50)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.IntegerField(db_column='ACTIVO')  # Field name made lowercase.
    fecha_creado = models.DateField(db_column='FECHA_CREADO', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='SUCURSAL_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_sucursal'
        verbose_name = 'Usuario de Sucursal'
        verbose_name_plural = 'Usuarios de Sucursales'


class Permiso(models.Model):
    num_permiso = models.IntegerField(db_column='NUM_PERMISO', primary_key=True)  # Field name made lowercase.
    permiso = models.CharField(db_column='PERMISO', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permiso'
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'


class DetallePermiso(models.Model):
    id_detalle_permiso = models.IntegerField(db_column='ID_DETALLE_PERMISO', primary_key=True)  # Field name made lowercase.
    sucursal_usuario = models.ForeignKey(UsuarioSucursal, models.DO_NOTHING, db_column='SUCURSAL_USUARIO', blank=True, null=True)  # Field name made lowercase.
    permiso_num = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='PERMISO_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_permiso'
        verbose_name = 'Detalle de Permiso'
        verbose_name_plural = 'Detalles de Permisos'