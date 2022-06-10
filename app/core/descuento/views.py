from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from core.descuento.models import Descuento
from core.descuento.forms import FormDescuento


class DescuentoList(ListView):
    model = Descuento
    template_name = 'all_descuentos.html'


class DescuentoCreate(SuccessMessageMixin,CreateView):
    model = Descuento
    form_class = FormDescuento
    template_name = 'form_descuento.html'
    success_url = reverse_lazy('descuento:addDescuento')
    success_message = 'Ingresado con éxito...'


class DescuentoUpdate(SuccessMessageMixin,UpdateView):
    model = Descuento
    form_class = FormDescuento
    template_name = 'edit_descuento.html'
    success_url =  reverse_lazy('descuento:listDescuento')
    success_message = 'Modificado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        descuento = get_object_or_404(Descuento,pk=id)
        return render(request,self.template_name,{'descuento':descuento})


class DescuentoDelete(DeleteView):
    model = Descuento
    template_name = 'delete_descuento.html'
    success_url = reverse_lazy('descuento:listDescuento')

