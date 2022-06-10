from django.contrib import admin
from core.persona.models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id_persona','nombre','apellido','fecha_nacimiento','edad','telefono_num']
    list_filter = ['fecha_nacimiento','edad']
    list_editable = ['nombre','apellido','fecha_nacimiento']
    list_per_page = 10
    search_fields = ['nombre','apellido','telefono_num']


admin.site.register(Persona,PersonaAdmin)