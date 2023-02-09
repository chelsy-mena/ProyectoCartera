from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

# Create your views here.

def tabla_indicadores(request):

    """Leer el nit y mostrar la tabla de indicadores"""

    indicadores = pd.read_csv(
        r'D:\Users\chelsy.mena\OneDrive - Centro de Servicios Mundial SAS\Documentos\Proyectos\Cartera\indicadores_2018_a_2020.csv',
        sep=";")

    pedazo_html = indicadores.to_html(index=False)

    return HttpResponse(pedazo_html)