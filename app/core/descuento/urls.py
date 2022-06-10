from django.urls import path
from core.descuento.views import DescuentoList,DescuentoCreate,DescuentoUpdate,DescuentoDelete

app_name='descuento'

urlpatterns = [
    path('list/',DescuentoList.as_view(),name='listDescuento'),
    path('add/',DescuentoCreate.as_view(),name='addDescuento'),
    path('edit/<str:pk>',DescuentoUpdate.as_view(),name='editDescuento'),
    path('delete/<str:pk>',DescuentoDelete.as_view(),name='deleteDescuento'),
]