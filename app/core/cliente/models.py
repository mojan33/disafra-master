from django.db import models
from core.persona.models import Persona


class Cliente(models.Model):
    nit_cliente = models.CharField(db_column='NIT_CLIENTE', primary_key=True, max_length=15)  # Field name made lowercase.
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='PERSONA_ID')  # Field name made lowercase.
    mayorista = models.BooleanField(db_column='MAYORISTA')  # Field name made lowercase.

    def __str__(self):
        return f'{self.nit_cliente} - {self.persona.nombre} {self.persona.apellido}'

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'