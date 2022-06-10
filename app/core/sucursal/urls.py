from django.urls import path
from core.sucursal.views import SucursalList,SucursalCreate,SucursalUpdate,SucursalDelete

app_name='sucursal'

urlpatterns = [
    path('list/',SucursalList.as_view(),name='listSucursal'),
    path('add/',SucursalCreate.as_view(),name='addSucursal'),
    path('edit/<int:pk>',SucursalUpdate.as_view(),name='editSucursal'),
    path('delete/<int:pk>',SucursalDelete.as_view(),name='deleteSucursal'),
]