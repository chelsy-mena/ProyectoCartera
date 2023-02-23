import pandas as pd

def borrar_fila(fila, df):

    """
    Actualiza el registro de un cliente, borrando la fila de ese año si ya está
    
    ARGS:
    fila -> DataFrame de pandas de una fila registrada por el usuario
    df -> DataFrame de pandas de la base de datos

    RETURNS
    df -> DataFrame con la BD total, sin la fila a reemplazar
    """

    año_registrado = fila.AÑO.tolist()[0]
    nit_registrado = fila.NIT.tolist()[0]

    tabla = df[(df.NIT == nit_registrado) & (df.AÑO == año_registrado)].copy()

    if tabla.shape[0] != 0:
        indice = tabla.index.tolist()[0]
        df = df.drop(index = indice)

    return df