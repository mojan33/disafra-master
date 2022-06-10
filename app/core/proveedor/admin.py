from django.contrib import admin
from core.proveedor.models import Proveedor,Visitador


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id_proveedor','nombre','correo','direccion','telefono_num']
    list_filter = []
    list_editable = ['nombre','correo','direccion','telefono_num']
    list_per_page = 10
    search_fields = ['nombre','correo','direccion','telefono_num']


class VisitadorAdmin(admin.ModelAdmin):
    list_display = ['id_visitador','persona','proveedor']
    list_filter = ['proveedor']
    list_editable = ['proveedor']
    list_per_page = 10
    search_fields = ['persona','proveedor']


admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Visitador,VisitadorAdmin)