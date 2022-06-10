from django.db import models
from core.telefono.models import Telefono
from core.direccion.models import Direccion


class Persona(models.Model):
    id_persona = models.IntegerField(db_column='ID_PERSONA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='FECHA_NACIMIENTO')  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD')  # Field name made lowercase.
    telefono_num = models.ForeignKey(Telefono, models.DO_NOTHING, db_column='TELEFONO_NUM', blank=True, null=True)  # Field name made lowercase.
    direccion_id = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='DIRECCION_ID', blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        #abstract = True  #Prueba de abstacción.