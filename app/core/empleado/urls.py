from django.urls import path
from core.empleado.views import EmpleadoList,EmpleadoCreate,EmpleadoUpdate,EmpleadoDelete

app_name='empleado'

urlpatterns = [
    path('list/',EmpleadoList.as_view(),name='listEmpleado'),
    path('add/',EmpleadoCreate.as_view(),name='addEmpleado'),
    path('edit/<int:pk>',EmpleadoUpdate.as_view(),name='editEmpleado'),
    path('delete/<int:pk>',EmpleadoDelete.as_view(),name='deleteEmpleado'),
]