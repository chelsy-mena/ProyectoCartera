from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

# Create your views here.

def busqueda(request1):

    return render(request1,"nits/busqueda.html")

def buscar(request1):
    mensaje="Articulo Buscado : %r" %request1.GET["prd"]
    

    return HttpResponse(mensaje)

def Home(request):
    return render(request,'nits/login.html')

def tabla_indicadores(request):

    """Leer el nit y mostrar la tabla de Maestro"""
    
    nit = request.GET["prd"]
    maestro = pd.read_csv(
        r'D:\Users\p.manufactura07\OneDrive - Centro de Servicios Mundial SAS\Escritorio\PruebaProyectoCartera\PythonMaestro7.csv',
        sep=",")
    maestro = maestro.astype({'NIT': str})
    print(maestro)
    tabla = maestro[maestro.NIT == nit]
    
  
    if tabla.shape[0] == 0:
        pedazo_html = "<h1>Ese NIT no está en la tabla</h1>"
    else:
        pedazo_html = tabla.T.to_html(index=False,classes=['maestro'])
    

    return render(request, "nits/index.html", {'tabla_a_mostrar': pedazo_html, 'nit': nit})


