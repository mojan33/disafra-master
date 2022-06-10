from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from core.persona.models import Persona
from core.direccion.models import Direccion, Departamento, Municipio
from core.telefono.models import TipoTelefono,Telefono
from core.empleado.models import Empleado,Puesto
from core.sucursal.models import Sucursal
from core.empleado.forms import FormEmpleado
from core.persona.forms import FormPersona
from core.telefono.forms import FormTelefono
from core.direccion.forms import FormDireccion


class EmpleadoList(ListView):
    model = Empleado
    template_name = 'all_empleados.html'


class EmpleadoCreate(SuccessMessageMixin,CreateView):
    model = Empleado
    form_class = FormEmpleado
    second_form_class = FormPersona
    third_form_class = FormTelefono
    four_form_class = FormDireccion
    template_name = 'form_empleado.html'
    success_url = reverse_lazy('empleado:addEmpleado')
    success_message = 'Ingresado con éxito...'

    def post(self, request, *args, **kwargs):
        state = False
        municipio = Municipio.objects.get(id_municipio=request.POST.get('municipio'))

        direccion = Direccion()
        direccion.id_direccion = request.POST.get('id_direccion')
        direccion.direccion = request.POST.get('direccion')
        direccion.referencia = request.POST.get('referencia')
        direccion.municipio = municipio
        direccion.save()

        tipo_telefono = TipoTelefono.objects.get(id_tipo_telefono=request.POST.get('tipo_telefono'))

        telefono = Telefono()
        telefono.num_telefono = request.POST.get('num_telefono')
        telefono.tipo_telefono = tipo_telefono
        telefono.save()

        tel = Telefono.objects.get(num_telefono=request.POST.get('num_telefono'))
        dir = Direccion.objects.get(id_direccion=request.POST.get('id_direccion'))

        persona = Persona()
        persona.id_persona = request.POST.get('id_persona')
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        persona.edad = request.POST.get('edad')
        persona.telefono_num = tel
        persona.direccion_id = dir
        persona.save()

        per = Persona.objects.get(id_persona=request.POST.get('id_persona'))
        suc = Sucursal.objects.get(id_sucursal=request.POST.get('sucursal'))
        pue = Puesto.objects.get(id_puesto=request.POST.get('puesto'))

        empleado = Empleado()
        empleado.cod_empleado = request.POST.get('cod_empleado')
        empleado.pass_field = request.POST.get('pass_field')
        empleado.correo = request.POST.get('correo')
        empleado.sucursal = suc
        empleado.puesto = pue
        empleado.persona = per
        empleado.save()

        return render(request,self.template_name,{'msn':'success'})

    def get(self, request, *args, **kwargs):
        municipios = Municipio.objects.all()
        departamentos = Departamento.objects.all()
        tipoTelefono = TipoTelefono.objects.all()
        sucursales = Sucursal.objects.all()
        puestos = Puesto.objects.all()

        idPersona = self.increment_persona()
        idEmpleado = self.increment_empleado()
        idDireccion = self.increment_direccion()
        return render(request,self.template_name,{'puestos':puestos,'sucursales':sucursales,'departamentos':departamentos,'municipios':municipios,'tipoTelefono':tipoTelefono,'idPersona':idPersona,'idDireccion':idDireccion,'idEmpleado':idEmpleado})

    def increment_persona(self):
        models = Persona.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_persona)

        return id+1

    def increment_empleado(self):
        models = Empleado.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.cod_empleado)

        return id+1

    def increment_direccion(self):
        models = Direccion.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_direccion)

        return id+1


class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = FormEmpleado
    template_name = 'edit_empleado.html'
    success_url =  reverse_lazy('empleado:listEmpleado')
    success_message = 'Modificado con éxito...'


class EmpleadoDelete(SuccessMessageMixin,DeleteView):
    model = Empleado
    template_name = 'delete_empleado.html'
    success_url = reverse_lazy('empleado:listEmpleado')
    success_message = 'Eliminado con éxito...'

