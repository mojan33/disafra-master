from django import forms
from core.descuento.models import Descuento


class FormDescuento(forms.ModelForm):

    class Meta:
        model = Descuento
        fields = [
            'cod_descuento',
            'porcentaje',
            'descripcion',
        ]
        labels = {
            'cod_descuento':'Código de descuento',
            'porcentaje':'Porcentaje',
            'descripcion':'Descripción',
        }
        widgets = {
            'cod_descuento':forms.TextInput(),
            'porcentaje':forms.NumberInput(),
            'descripcion':forms.Textarea(),
        }