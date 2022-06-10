from django.db import models


class Categoria(models.Model):
    id_categoria = models.IntegerField(verbose_name='ID',db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(verbose_name='Nombre',db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    descripcion = models.CharField(verbose_name='Descripción',db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoria_sub = models.ForeignKey('self', models.DO_NOTHING, db_column='CATEGORIA', blank=True, null=True, verbose_name='Categoria')  # Field name made lowercase.

    def __str__(self):
        return f'{self.id_categoria} - {self.nombre}'

    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'