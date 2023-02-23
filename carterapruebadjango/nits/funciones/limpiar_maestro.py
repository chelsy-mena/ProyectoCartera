import pandas as pd
import regex as re

def limpiar_maestro(df):

    """ 
    Limpiar el Maestro de Clientes

    ARGS
    df -> DataFrame con el maestro de clientes entero

    RETURNS
    maestro -> DataFrame con el maestro de clientes a mostrar
    """

    df["NUMERO_CUENTA"] = df.NUMERO_CUENTA.apply(lambda x: re.sub("-[0-9]", "", str(x)))
    df = df.astype({"FECHA_ANTIGUEDAD": str})
    df = df[["NUMERO_CUENTA", "NOMBRE_CLIENTE", 'CLASF_CLIENTE', 'CLPERFIL', 'CUPO_CREDITO','TER_GENERAL', 'FECHA_ANTIGUEDAD']]
    df.drop_duplicates(inplace=True)

    df.rename(columns = {
        "NUMERO_CUENTA": 'NIT',
        "NOMBRE_CLIENTE": 'NOMBRE CLIENTE',
        'CLASF_CLIENTE': 'CLASIFICACIÓN',
        'CLPERFIL': 'PERFIL',
        'CUPO_CREDITO': 'CUPO CREDITO',
        'TER_GENERAL': 'TÉRMINO',
        'FECHA_ANTIGUEDAD': 'FECHA DE ANTIGUEDAD'
        }, inplace = True)

    df['CUPO CREDITO'] = df['CUPO CREDITO'].apply(lambda x: "$ "+'{:,.0f}'.format(x))
    df['NOMBRE CLIENTE'] = df['NOMBRE CLIENTE'].apply(lambda x: x.replace('?', '&'))
    
    return df