import pandas as pd

def calcular_totales(fila):

    """
    Calcula las columnas compuestas para un registro del usuario
    
    ARGS
    fila -> JSON de un elemento que tiene los datos registrados por el usuario

    RETURNS
    fila_df -> DataFrame de una fila con lo registrado por el usuario y las columnas calculadas
    """

    fila_df = pd.DataFrame(fila)
    fila_df.columns = [x.replace('_', ' ') for x in fila_df.columns]


    # Estado de Resultados

    fila_df['Total Activo Corriente'] = fila_df['Efectivo y equivalentes al efectivo'] + \
                                        fila_df['Clientes CP'] + \
                                        fila_df['Inventarios CP'] + \
                                        fila_df['Otros activos financieros'] + \
                                        fila_df['Otros Activos Corrientes']


    fila_df['Total Activo No Corriente'] = fila_df['Otros Activos No Corrientes'] + \
                                           fila_df['Deudores LP'] + \
                                           fila_df['Propiedad planta y equipo']

    fila_df['Total Activo'] = fila_df['Total Activo Corriente'] + fila_df['Total Activo No Corriente']

    fila_df['Total Pasivo Corriente'] = fila_df['Obligaciones Financieras CP'] + \
                                        fila_df['Proveedores CP'] + \
                                        fila_df['Otros Pasivos Corrientes']
    
    fila_df['Total Pasivo No Corriente'] = fila_df['Obligaciones Financieras LP'] + \
                                           fila_df['Proveedores LP'] + \
                                           fila_df['Otros pasivos no Corrientes']
    
    fila_df['Total Pasivo'] = fila_df['Total Pasivo Corriente'] + fila_df['Total Pasivo No Corriente']

    fila_df['Total patrimonio'] = fila_df['Capital Social'] + \
                                  fila_df['Prima de emisión'] + \
                                  fila_df['Reservas'] + \
                                  fila_df['Ganancias acumuladas'] + \
                                  fila_df['Otros Patrimonio']

    fila_df['Total Pasivo mas Patrimonio'] = fila_df['Total patrimonio'] + fila_df['Total Pasivo']


    # Balance

    fila_df['Utilidad Bruta'] = fila_df['Ingresos Operacionales'] - fila_df['Costos de ventas y de prestación de servicios']

    fila_df['Utilidad Operacional'] = (fila_df['Utilidad Bruta'] + fila_df['Otros ingresos']) - \
                                      (fila_df['Gastos Operacionales de admon'] + \
                                       fila_df['Gastos Operacionales de venta'] + \
                                       fila_df['Otros gastos'])

    fila_df['Utilidad antes de impuestos'] = fila_df['Utilidad Operacional'] + \
                                             fila_df['Ingresos financieros'] - \
                                             fila_df['Costos financieros'] + \
                                             fila_df['Otros ingresos o egresos']


    fila_df['Ganancias y pérdidas'] = fila_df['Utilidad antes de impuestos'] + \
                                      fila_df['Impuesto de renta y complementarios']


    return fila_df
    