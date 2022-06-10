from django import forms
from core.persona.models import Persona


class FormPersona(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'id_persona',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'edad'
        ]
        labels = {
            'id_persona':'ID',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'fecha_nacimiento':'Fecha de nacimiento',
            'edad':'Edad'
        }
        widgets = {
            'id_persona':forms.HiddenInput(),
            'nombre':forms.TextInput(),
            'apellido':forms.TextInput(),
            'fecha_nacimiento':forms.TextInput(),
            'edad':forms.NumberInput()
        }