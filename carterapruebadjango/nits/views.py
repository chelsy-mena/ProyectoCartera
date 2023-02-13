from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

# Create your views here.

def Home(request):
    return render(request,'nits/index.html')

def tabla_indicadores(request, nit):

    """Leer el nit y mostrar la tabla de indicadores"""

    indicadores = pd.read_csv(
        r'C:\Users\KEVIN\Desktop\PruebaProyectoCartera\PythonMaestro7.csv',
        sep=",")
    indicadores = indicadores.astype({'NIT': str})
    print(indicadores)
    tabla = indicadores[indicadores.NIT == nit]
    
    if tabla.shape[0] == 0:
        pedazo_html = "<h1>Ese NIT no está en la tabla</h1>"
    else:
        pedazo_html = tabla.to_html(index=False)
    

    return render(request, "nits/index.html", {'tabla_a_mostrar': pedazo_html, 'nit': nit})