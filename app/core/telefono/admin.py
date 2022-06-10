from django.contrib import admin
from core.telefono.models import Telefono,TipoTelefono


class TipoTelefonoAdmin(admin.ModelAdmin):
    list_display = ['id_tipo_telefono','tipo']
    list_filter = []
    list_editable = ['tipo']
    list_per_page = 10
    search_fields = ['tipo']


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ['num_telefono','tipo_telefono','extension']
    list_filter = ['tipo_telefono']
    list_editable = ['extension']
    list_per_page = 10
    search_fields = ['tipo_telefono']


admin.site.register(TipoTelefono,TipoTelefonoAdmin)
admin.site.register(Telefono,TelefonoAdmin)