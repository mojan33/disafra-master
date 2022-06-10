from django.urls import path
from core.cliente.views import ClienteList,ClienteCreate,ClienteUpdate,ClienteDelete

app_name='cliente'

urlpatterns = [
    path('list/',ClienteList.as_view(),name='listCliente'),
    path('add/',ClienteCreate.as_view(),name='addCliente'),
    path('edit/<str:pk>',ClienteUpdate.as_view(),name='editCliente'),
    path('delete/<str:pk>',ClienteDelete.as_view(),name='deleteCliente'),
]