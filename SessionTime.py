import datetime as dt
from FileControl import open_file
from UserManager import search_usuario
import re
import pandas as pd

class ErrorFecha(Exception):
    pass

def RegexFecha(fecha): 
    fecha_regex = re.compile(r'^\d{4}(\-|/)(0?[1-9]|1[0-1-2])(\-|/)(0?[1-9]|[1-2][0-9]|3[0-1])$')
    if fecha_regex.match(fecha):
        print('Valor ingresado correctamente')
    else:
        fecha = "2019-08-28"
        raise ErrorFecha('El valor ingresado es incorrecto, se ingresará por defecto la primer fecha del excel')
    
    return fecha

def sum_session_time(datos, x: str, y: str):
    sess_time = 0
    inicio = re.split("-|/| ", x) #separa los terminos y los convierte en objetos de una lista 
    fin = re.split("-|/| ", y)

    fecha_ini = dt.datetime(int(inicio[0]), int(inicio[1]), int(inicio[2])).date() #vuelve los datos a numeros enteros
    fecha_fin = dt.datetime(int(fin[0]), int(fin[1]), int(fin[2])).date()
   
    for i in datos:
        if pd.to_datetime(i[1]).date() >= fecha_ini and pd.to_datetime(i[2]).date() <= fecha_fin:
            sess_time += i[3]
    
    return sess_time
