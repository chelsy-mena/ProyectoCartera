import pandas as pd
import numpy as np

def calcular_indicadores(fila):

    """
    Calcula los indicadores financieros para un registro del usuario
    
    ARGS
    fila -> DataFrame de una fila que tiene los datos registrados por el usuario y los totales calculados   

    RETURNS
    indicadores -> DataFrame de una fila con los indicadores
    """

    indicadores = pd.DataFrame()

    indicadores['NIT'] = fila['NIT']
    indicadores['AÑO'] = fila['AÑO']

    indicadores['K DE W / VENTAS'] = (fila['Clientes CP'] + fila['Inventarios CP'] 
                                - fila['Proveedores CP'] - fila['Proveedores LP'])*100 / \
                                fila['Ingresos Operacionales']

    indicadores['CAPITAL DE TRABAJO'] = fila['Clientes CP'] + fila['Inventarios CP'] - \
                                        fila['Proveedores CP'] - fila['Proveedores LP']
                                    
    indicadores['RAZON CORRIENTE'] = (fila['Total Activo Corriente'])/(fila['Total Pasivo Corriente'])

    indicadores['PRUEBA ACIDA'] = (fila['Total Activo Corriente'] - fila['Inventarios CP']
                                )/(fila['Total Pasivo Corriente'])

    indicadores['DIAS INVENTARIO'] = 360/(fila['Costos de ventas y de prestación de servicios']/ \
                                        fila['Inventarios CP'])

    indicadores['DIAS CARTERA'] = 360/(fila['Ingresos Operacionales']/fila['Clientes CP'])

    indicadores['DIAS PROVEEDORES'] = 360/(fila['Costos de ventas y de prestación de servicios']/(
                                    fila['Proveedores CP'] + fila['Proveedores LP']))

    indicadores['ENDEUDAMIENTO TOTAL'] = (fila['Total Pasivo']*100)/fila['Total Activo']

    indicadores['ENDEUDAMIENTO FINANCIERO'] =(fila[ 'Obligaciones Financieras CP'] + fila['Obligaciones Financieras LP']
                                            )*100/fila['Total Pasivo']

    indicadores['MARGEN BRUTO'] = fila['Utilidad Bruta']*100/fila['Ingresos Operacionales']

    indicadores['MARGEN OPERACIONAL'] = (fila['Utilidad Operacional']*100)/fila['Ingresos Operacionales']

    indicadores['MARGEN NETO'] = fila['Ganancias y pérdidas']*100/fila['Ingresos Operacionales']

    indicadores.fillna(0, inplace = True)

    tabla_infs = indicadores[indicadores['DIAS PROVEEDORES'].apply(lambda x: np.isinf(x))]
    for i in tabla_infs.index:
        indicadores['DIAS PROVEEDORES'].iloc[i] = 1000.0

    tabla_infs = indicadores[indicadores['DIAS INVENTARIO'].apply(lambda x: np.isinf(x))]
    for i in tabla_infs.index:
        indicadores['DIAS INVENTARIO'].iloc[i] = 1000.0

    indicadores = indicadores.astype({
        'DIAS INVENTARIO': int, 
        'DIAS CARTERA': int,
        'DIAS PROVEEDORES': int,
        'K DE W / VENTAS': int
        })

    for column in ['RAZON CORRIENTE','PRUEBA ACIDA',
        'ENDEUDAMIENTO TOTAL','ENDEUDAMIENTO FINANCIERO', 
        'MARGEN BRUTO', 'MARGEN OPERACIONAL', 'MARGEN NETO']:
        indicadores[column] = round(indicadores[column], 1)

    return indicadores

