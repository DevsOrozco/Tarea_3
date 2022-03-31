"""Ejercicio 6
Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro."""
from math import pi

def calculos(radio):#Se crea la funcion calculos
    area=pi*radio*radio#Se calcula el área y perímetro del círculo
    perimetro=2*pi*radio
    print("El área es:",round(area,2),"\n", "El perímetro es:",round(perimetro,2))#Se imprime el área y perímetro
def main():#Se crea el programa principal
    print("*Operaciones con Circunferencias*")
    rad=int(input("Por favor ingrese el radio de la circunferencia: "))#Se ingresa el radio del círculo
    calculos(rad)#Se ingresa el radio y ejecuta la función cálculos
main()#Se ejecuta la función principal