from django.urls import path
from core.categoria.views import CategoriaList,CategoriaCreate,CategoriaUpdate,CategoriaDelete

app_name='categoria'

urlpatterns = [
    path('list/',CategoriaList.as_view(),name='listCategoria'),
    path('add/',CategoriaCreate.as_view(),name='addCategoria'),
    path('edit/<int:pk>',CategoriaUpdate.as_view(),name='editCategoria'),
    path('delete/<int:pk>',CategoriaDelete.as_view(),name='deleteCategoria'),
]