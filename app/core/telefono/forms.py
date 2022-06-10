from django import forms
from core.telefono.models import Telefono


class FormTelefono(forms.ModelForm):

    class Meta:
        model = Telefono
        fields = [
            'num_telefono',
            'tipo_telefono',
        ]
        labels = {
            'num_telefono':'Número de teléfono',
            'tipo_telefono':'Compañía'
        }
        widgets = {
            'num_telefono':forms.TextInput(),
            'tipo_telefono':forms.Select()
        }