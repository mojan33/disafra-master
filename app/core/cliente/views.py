from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from core.persona.models import Persona
from core.direccion.models import Direccion, Departamento, Municipio
from core.telefono.models import TipoTelefono,Telefono
from core.cliente.models import Cliente
from core.cliente.forms import FormCliente
from core.persona.forms import FormPersona
from core.telefono.forms import FormTelefono
from core.direccion.forms import FormDireccion


class ClienteList(ListView):
    model = Cliente
    template_name = 'all_clientes.html'


class ClienteCreate(SuccessMessageMixin,CreateView):
    model = Cliente
    form_class = FormCliente
    second_form_class = FormPersona
    third_form_class = FormTelefono
    four_form_class = FormDireccion
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('cliente:addCliente')
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

        mayorista = request.POST.get('mayorista')

        if mayorista == 'on':
            mayorista = True
        else:
            mayorista = False

        cliente = Cliente()
        cliente.nit_cliente = request.POST.get('nit_cliente')
        cliente.mayorista = mayorista
        cliente.persona = per
        cliente.save()

        return render(request,self.template_name,{'msn':'success'})

    def get(self, request, *args, **kwargs):
        municipios = Municipio.objects.all()
        departamentos = Departamento.objects.all()
        tipoTelefono = TipoTelefono.objects.all()

        idPersona = self.increment_persona()
        idDireccion = self.increment_direccion()
        return render(request,self.template_name,{'departamentos':departamentos,'municipios':municipios,'tipoTelefono':tipoTelefono,'idPersona':idPersona,'idDireccion':idDireccion})

    def increment_persona(self):
        models = Persona.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_persona)

        return id+1

    def increment_direccion(self):
        models = Direccion.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_direccion)

        return id+1


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'form_cliente.html'
    success_url =  reverse_lazy('cliente:listCliente')


class ClienteDelete(SuccessMessageMixin,DeleteView):
    model = Cliente
    template_name = 'delete_cliente.html'
    success_url = reverse_lazy('cliente:listCliente')
    success_message = 'Eliminado con éxito...'

