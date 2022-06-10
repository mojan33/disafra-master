from django.contrib import admin
from core.cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nit_cliente','persona','mayorista']
    list_filter = ['mayorista']
    list_editable = ['mayorista']
    list_per_page = 10
    search_fields = ['nit_cliente','mayorista']


admin.site.register(Cliente,ClienteAdmin)
