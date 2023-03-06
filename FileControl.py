import pandas as pd

def open_file(path, sheet):
    datos = pd.ExcelFile(path)
    df = datos.parse(sheet)
    columnas = df[['Usuario', 'Inicio de Conexi¢n', 'Fin de Conexio', 'Session Time']]
    return columnas

def export_file(usuario, inicio, fin, time):
    df = pd.DataFrame({'Usuario': [usuario],
                        'Fecha en la que comienza la conexión':[inicio],
                        'Fecha en la que termina la conexión': [fin],
                        'Tiempo total conectado':[time]})
    nombre = usuario
    df.to_excel('time_conect.xlsx', sheet_name=nombre, index=False)
    return
