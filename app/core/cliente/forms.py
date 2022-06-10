from django import forms
from core.cliente.models import Cliente


class FormCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nit_cliente',
            'mayorista'
        ]
        labels = {
            'nit_cliente': 'NIT',
            'mayorista': 'Mayorista'
        }
        widgets = {
            'nit_cliente': forms.TextInput(),
            'mayorista': forms.CheckboxInput()
        }