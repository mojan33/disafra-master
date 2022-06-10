from django import forms
from core.sucursal.models import Sucursal


class FormSucursal(forms.ModelForm):

    class Meta:
        model = Sucursal
        fields = [
            'id_sucursal',
            'nombre',
            'correo',
        ]
        labels = {
            'id_sucursal':'ID',
            'nombre':'Nombre',
            'correo':'E-mail',
        }
        widgets = {
            'id_sucursal':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'correo':forms.Textarea(),
        }