from django import forms
from core.direccion.models import Direccion


class FormDireccion(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = [
            'id_direccion',
            'municipio',
            'direccion',
            'referencia',
        ]

        labels = {
            'id_direccion':'ID',
            'direccion':'Dirección',
            'referencia':'Referencia',
            'municipio':'Municipio',
        }

        widgets = {
            'id_direccion':forms.HiddenInput(),
            'direccion':forms.TextInput(),
            'referencia':forms.Textarea(),
            'municipio':forms.Select(),
        }