"""Ejercicio 3
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima 
y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""

from pip import main #Importamos main de pip
def Temperatura (Tmin,Tmax):#Se crea la función temperatura
    Tmed=(Tmax+Tmin)/2#Se calcula la temperatura media
    print("La temperatura media es:",Tmed)#Se imprime un string que indica la temperatura

def main ():#Se crea el programa principal en la función main
    print("*Temperatura diaria*")
    n1=int(input("Ingrese el número de días que se desean introducir: "))#Se ingesa el número de días a calcular
    for i in range(0,n1):#Se inicia el ciclo for
        n2=int(input("Ingrese la temperatura mínima: "))#Se introducen los valores de temperatura mínima y máxima
        n3=int(input("Ingrese la temperatura máxima: "))
        Temperatura(n2,n3)#Se ejecuta la función temperatura
main()

