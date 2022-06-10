from django import forms
from core.empleado.models import Empleado


class FormEmpleado(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = [
            'cod_empleado',
            'pass_field',
            'correo',
        ]
        labels = {
            'cod_empleado':'Código de empleado',
            'pass_field':'Contraseña',
            'correo':'E-mail',
        }
        widgets = {
            'cod_empleado':forms.TextInput(),
            'pass_field':forms.PasswordInput(),
            'correo':forms.EmailInput(),
        }