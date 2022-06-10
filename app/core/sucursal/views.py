from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from core.direccion.models import Direccion,Municipio,Departamento
from core.telefono.models import TipoTelefono,Telefono
from core.sucursal.models import Sucursal
from core.sucursal.forms import FormSucursal


class SucursalList(ListView):
    model = Sucursal
    template_name = 'all_sucursales.html'


class SucursalCreate(SuccessMessageMixin,CreateView):
    model = Sucursal
    form_class = FormSucursal
    template_name = 'form_sucursal.html'
    success_url = reverse_lazy('sucursal:addSucursal')
    success_message = 'Ingresado con éxito...'

    def get(self, request, *args, **kwargs):
        municipios = Municipio.objects.all()
        departamentos = Departamento.objects.all()
        tipoTelefono = TipoTelefono.objects.all()

        idDireccion = self.increment_direccion()
        idSucursal = self.increment_sucursal()
        return render(request,self.template_name,{'departamentos':departamentos,'municipios':municipios,'tipoTelefono':tipoTelefono,'idDireccion':idDireccion,'idSucursal':idSucursal})

    def increment_sucursal(self):
        models = Sucursal.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_sucursal)

        return id+1

    def increment_direccion(self):
        models = Direccion.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_direccion)

        return id+1

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

        sucursal = Sucursal()
        sucursal.id_sucursal = request.POST.get('id_sucursal')
        sucursal.nombre = request.POST.get('nombre')
        sucursal.correo = request.POST.get('correo')
        sucursal.direccion = dir
        sucursal.telefono_num = tel
        sucursal.save()

        return render(request,self.template_name,{'msn':'success'})


class SucursalUpdate(UpdateView):
    model = Sucursal
    form_class = FormSucursal
    template_name = 'form_sucursal.html'
    success_url =  reverse_lazy('sucursal:listSucursal')


class SucursalDelete(SuccessMessageMixin,DeleteView):
    model = Sucursal
    template_name = 'delete_sucursal.html'
    success_url = reverse_lazy('sucursal:listSucursal')
    success_message = 'Eliminado con éxito...'

