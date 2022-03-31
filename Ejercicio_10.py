"""Ejercicio 10
Escribir dos funciones que permitan calcular:
La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.
"""
def segundos(h,min,s):#Creo la funcion segundos
    horas=h*3600#Creo la fracción de las horas
    minutos=min*60#Creo la fracción de los minutos
    segundos=horas+minutos+s#Sumo la fraccion de horas, minutos y segundos
    return segundos#Devuelvo los segundos

def H_MIN_SEC(sec):#Creo la función para extraer la hora,minutos y segundos
    horas=int(sec/3600)#Extraigo la parte entera de las horas
    r=(sec/3600)-horas#Extraigo la parte fraccionaria de las horas
    minutos=int(r*60)#Hago el cálculo de los minutos en forma de enteros
    r2=(r*60)-minutos#Extraigo la parte fraccionaria de los minutos
    segundos=int(r2*60)#Extraigo los segundos
    return horas, minutos,segundos#Devuelvo las horas, minutos y segundos
def main():
    print("Segundos:",segundos(2,30,15))#Llamo a la funcion de segundos
    print("Horas,Minutos, Segundos:",H_MIN_SEC(9015))#Llamo a la función horas, minutos segundos
main()