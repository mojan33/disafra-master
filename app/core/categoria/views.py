from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from core.categoria.models import Categoria
from core.categoria.forms import FormCategoria


class CategoriaList(ListView):
    model = Categoria
    template_name = 'all_categoria.html'


class CategoriaCreate(SuccessMessageMixin,CreateView):
    model = Categoria
    form_class = FormCategoria
    template_name = 'form_categoria.html'
    success_url = reverse_lazy('categoria:addCategoria')
    success_message = 'Ingresado con éxito...'

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        auto_increment = self.increment()
        return render(request,self.template_name,{'categorias':categorias,'auto_increment':auto_increment})

    def increment(self):
        models = Categoria.objects.all()
        id=0
        if models:
            for model in models:
                id = int(model.id_categoria)

        return id+1


class CategoriaUpdate(SuccessMessageMixin,UpdateView):
    model = Categoria
    form_class = FormCategoria
    template_name = 'edit_categoria.html'
    success_url =  reverse_lazy('categoria:listCategoria')
    success_message = 'Modificado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        categorias = Categoria.objects.all()
        categoria = get_object_or_404(Categoria,pk=id)
        return render(request,self.template_name,{'categoria':categoria,'categorias':categorias})


class CategoriaDelete(SuccessMessageMixin,DeleteView):
    model = Categoria
    template_name = 'delete_categoria.html'
    success_url = reverse_lazy('categoria:listCategoria')
    success_message = 'Eliminado con éxito...'

