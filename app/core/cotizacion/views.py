from django.shortcuts import render


def formCotizacion(request):
    return render(request,'form_cotizacion.html')