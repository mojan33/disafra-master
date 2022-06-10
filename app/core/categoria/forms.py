from django import forms
from core.categoria.models import Categoria


class FormCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'id_categoria',
            'nombre',
            'descripcion',
            'categoria_sub',
        ]
        labels = {
            'id_categoria':'ID',
            'nombre':'Nombre',
            'descripcion':'Descripción',
            'categoria_sub':'Categoria'
        }
        widgets = {
            'id_categoria':forms.NumberInput(
                attrs={
                    'id':'id_categoria',
                }
            ),
            'nombre':forms.TextInput(),
            'descripcion':forms.Textarea(),
            'categoria_sub':forms.Select()
        }