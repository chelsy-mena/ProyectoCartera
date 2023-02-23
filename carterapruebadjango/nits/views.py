from django.shortcuts import render
from django.http import HttpResponse
from nits.formularios.formularioPDF import FormularioPDF

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from .funciones.ruta_archivos import ruta_bd, ruta_indicadores, ruta_maestro
from .funciones.limpiar_maestro import limpiar_maestro
from .funciones.borrar_fila import borrar_fila
from .funciones.calcular_totales import calcular_totales
from .funciones.calcular_indicadores import calcular_indicadores

# Create your views here.
def Home(request):
    return render(request,'inicio.html')

def historico(request):
    return render(request,'historico.html')

def buscar(request1):

    mensaje="Articulo Buscado : %r" %request1.GET["prd"]
    return HttpResponse(mensaje)

def output(request):
    
    nit = request.GET["prd"]

    # TABLA MAESTRO
    #maestro = pd.read_csv( 
        #r'nits\static\data\data_maestro.csv',
        #sep=";")
    #maestro = maestro.astype({'NIT': str})
    #print(maestro)
    #tabla['CUPO'] = tabla['CUPO'].apply(lambda x: "$ "+'{:,.0f}'.format(x) )
    #tabla['NOMBRE'] = tabla['NOMBRE'].apply(lambda x: x.replace('?', '&') )
    
    maestro = pd.read_excel(ruta_maestro, sheet_name='Facturación')
    maestro = limpiar_maestro(maestro)
    
    tabla = maestro[maestro.NIT == nit]
    tabla = tabla.transpose()
    tabla.reset_index(drop=False, inplace=True)
    
    if tabla.shape[0] == 0:
        maestro_html = "<h5>Ese NIT no está en los datos</h5>"
    else:
        maestro_html = tabla.to_html(
            index=False,
            header=False,
            classes=['table table-striped tabla'])


    # TABLA INDICADORES
    # indicadores = pd.read_csv(
    #     ruta_archivos.ruta_indicadores,
    #     #r'nits\static\data\data_indicadores.csv',
    #     sep=";")

    indicadores = pd.read_csv(ruta_indicadores, sep=";")
    indicadores = indicadores.astype({'NIT': str, 'AÑO': str})

    tabla = indicadores[indicadores.NIT == nit].drop(columns = ['NIT'])
    tabla['CAPITAL DE TRABAJO'] = tabla['CAPITAL DE TRABAJO'].apply(lambda x: "$ "+'{:,.0f}'.format(x))

    for columna in ['K DE W / VENTAS', 'ENDEUDAMIENTO TOTAL',
                    'ENDEUDAMIENTO FINANCIERO', 
                    'MARGEN BRUTO','MARGEN OPERACIONAL', 'MARGEN NETO']:
        tabla[columna] = tabla[columna].apply(lambda x: '{:,}'.format(x) + " %")
    
    tabla_dos = tabla.transpose()
    tabla_dos.reset_index(drop=False, inplace=True)

    if tabla_dos.shape[0] == 0:
        indicadores_html = "<h5>Ese NIT no está en los datos</h5>"
    else:
        indicadores_html = tabla_dos.to_html(            
            index=False, 
            header=False,
            classes=['table table-striped tabla'])


    # GRAFICA INDICADORES
    fig = go.Figure()

    custom_template = {
    "layout": go.Layout(
        font={
            "family": 'Kanit',
            "size": 15
        },
        plot_bgcolor="#FBFBFB",
        paper_bgcolor="#FBFBFB"
    )}

    fig.update_layout(
        template = custom_template,
        width = 1100,
        height = 500)

    for column in tabla.columns.tolist():
        if column == 'AÑO':
            continue
        else:
            fig.add_trace(
                go.Bar(
                     x = tabla['AÑO'],
                     y = tabla[column],
                     name = column))

    grafica_html = pio.to_html(fig, include_plotlyjs=False, full_html=False)

    return render(request, "historico.html", {'tabla_maestro': maestro_html,
                                              'tabla_indicadores': indicadores_html,
                                              'grafica_indicadores': grafica_html,
                                              'nit': nit})


def registrar(request):

    lanzandoAlerta=False

    formulario=FormularioPDF()

    diccionario={
        "formulario":formulario,
        "bandera":lanzandoAlerta
    }

    if request.method=='POST':

        datosRecibidos=FormularioPDF(request.POST)

        if datosRecibidos.is_valid():
            datos = datosRecibidos.cleaned_data
            diccionario["bandera"] = True

            bd = pd.read_csv(ruta_bd, sep=";")
            bd = bd.astype({'AÑO': str, 'NIT': str})
            bd = borrar_fila(datos, bd)

            indicadores = pd.read_csv(ruta_indicadores, sep=";")
            indicadores = indicadores.astype({'AÑO': str, 'NIT': str})
            indicadores = borrar_fila(datos, indicadores)
            
            fila_agregar = calcular_totales(datos)
            fila_indicadores = calcular_indicadores(fila_agregar)

            bd = pd.concat([bd, fila_agregar])
            indicadores = pd.concat([indicadores, fila_indicadores])

            bd.to_csv(ruta_bd, index=False, encoding='utf-8', sep=';')
            indicadores.to_csv(ruta_indicadores, index=False, encoding='utf-8', sep=";")

    return render(request,'registrar.html', diccionario)