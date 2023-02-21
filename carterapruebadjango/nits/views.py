from django.shortcuts import render
from django.http import HttpResponse


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Create your views here.
def Home(request):
    return render(request,'inicio.html')
def historico(request):
    return render(request,'historico.html')
def registrar(request):
    return render(request,'registrar.html')
def buscar(request1):
    mensaje="Articulo Buscado : %r" %request1.GET["prd"]
    return HttpResponse(mensaje)
def output(request):

    """Leer el nit y mostrar la tabla de Maestro"""
    
    nit = request.GET["prd"]

    maestro = pd.read_csv(
        r'D:\Users\p.manufactura07\OneDrive - Centro de Servicios Mundial SAS\Escritorio\PruebaProyectoCartera\MaestroClientes.csv',
        sep=";")
    maestro = maestro.astype({'NIT': str})
    print(maestro)
    tabla = maestro[maestro.NIT == nit]
    tabla['CUPO'] = tabla['CUPO'].apply(lambda x: "$ "+'{:,.0f}'.format(x) )
    tabla['NOMBRE'] = tabla['NOMBRE'].apply(lambda x: x.replace('?', '&') )
    tabla = tabla.transpose()
    tabla.reset_index(drop=False, inplace=True)
    if tabla.shape[0] == 0:
        maestro_html = "<h5>Ese NIT no está en los datos</h5>"
    else:
        maestro_html = tabla.to_html(index=False, header=False, classes=['table table-striped  tabla'])


    indicadores = pd.read_csv(
        r'D:\Users\p.manufactura07\OneDrive - Centro de Servicios Mundial SAS\Escritorio\PruebaProyectoCartera\indicadores_2018_a_2020.csv',
        sep=";")
    indicadores = indicadores.astype({'NIT': str})
    tabla = indicadores[indicadores.NIT == nit].drop(columns = ['NIT'])
    tabla = tabla.transpose()
    tabla.reset_index(drop=False, inplace=True)
    if tabla.shape[0] == 0:
        indicadores_html = "<h5>Ese NIT no está en los datos</h5>"
    else:
        pedazo_html = tabla.to_html( index=False)
    
    
    fig = go.Figure()

    for column in indicadores.columns:
        if (column != 'NIT') and (column != 'AÑO'):
            fig.add_trace(
                go.Bar(
                    x=tabla['AÑO'],
                    y = tabla[column],
                    name = column))

    fig.update_layout(plot_bgcolor='#FFFFFF',
                width = 1000,
                height = 400,
                margin= {'l':20, 'r':20, 't':50, 'b':20})
    #fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='#dfebec', title = 'Año')
    #fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#dfebec', title = 'Valor del Indicador', secondary_y=False)

    html_grafica = pio.to_html(fig, include_plotlyjs=False, full_html=False)

    # opciones = indicadores.columns.tolist()
    # opciones_dict = {}

    # for opcion in opciones:
    #     opciones_dict[opcion]= {'id': opciones.index(opcion),
    #                            'name': opcion}

    
    return render(request,
                 "nits/index.html",
                 {#'options': opciones_dict,
                 'tabla_a_mostrar': pedazo_html,
                 'grafica': html_grafica,
                 'nit': nit})
