import pandas as pd

def borrar_fila(fila, df):

    """
    Actualiza el registro de un cliente, borrando la fila de ese año si ya está
    
    ARGS:
    fila -> JSON de un item registrado por el usuario
    df -> DataFrame de pandas de la base de datos

    RETURNS
    df -> DataFrame con la BD total, sin la fila a reemplazar
    """

    fila = pd.DataFrame(fila, index=[0])
    fila = fila.astype({'AÑO': str, 'NIT': str})

    año_registrado = fila.AÑO.tolist()[0]
    nit_registrado = fila.NIT.tolist()[0]

    print(fila, año_registrado, nit_registrado)

    tabla = df[(df.NIT == nit_registrado) & (df.AÑO == año_registrado)].copy()

    print(tabla.shape[0])

    if tabla.shape[0] != 0:
        indice = tabla.index.tolist()[0]
        print(indice)
        df = df.drop([indice])

    return df