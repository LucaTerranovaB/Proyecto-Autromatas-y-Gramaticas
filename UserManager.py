import re
import pandas as pd
from FileControl import open_file

class ErrorUsuario(Exception):
    pass
class ErrorFecha(Exception):
    pass

def RegexUsuario(usuario):
    regex_usuario = re.compile((r'\b([A-Za-z\.\/\d*]{1,})\b')) 
    try:
        if regex_usuario == usuario:
            pass
    except ErrorUsuario:
        print("El formato de usuario ingresado no es correcto, intente nuevamente")
    
    return usuario

def RegexFecha(fecha):
    regex_fecha = re.compile(r'\b([0-9]{4})-([0-9]{2})-([0-9]{2})\b')
    try:
        if regex_fecha == fecha:
            pass
    except ErrorFecha:
        print("El formato de fecha ingresado no es correcto, intente nuevamente")
    
    return fecha


def search_usuario(nombre: str, data):
    resultados = []
    df = pd.DataFrame(data) #convierte dichos datos en un dataframe
    lista = df.to_numpy().tolist() #convierte el DF en lista
    name = re.compile(nombre) #regex para buscar el nombre
    for i in lista:
        if i[2] != '\\N' and name.match(str(i[0])): 
            resultados.append([i[0], i[1], i[2], i[3]])
    
    return resultados

