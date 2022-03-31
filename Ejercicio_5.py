"""Ejercicio 5
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""
def calculadoraMaxMin(lista_num):#Se crea la función para calcular los valores máximo y mínimo
        maximo=max(lista_num)#Se almacena el número máximo de la lista con la función max()
        minimo=min(lista_num)#Se almacena el número mínimo de la lista con la función min()
        print("Máximo:",maximo)#Se imprime el número máximo
        print("Mínimo",minimo)#Se imprime el número mínimo

def main():#Se crea el programa principal
    print("*Máximo y mínimo de una lista*")
    n1=int(input("Por favor, ingrese la cantidad de valores que deseas analizar: "))#Se pide al usuario que ingrese la cantidad de valores que desea analizar
    lista=[]#Se crea una lista vacía
    print("Por favor, ingrese los valores: ")
    for i in range(0,n1):#Se crea el ciclo for para almacenar los valores ingresados por el usuario en la lista
        n2=int(input())
        lista.append(n2)
    calculadoraMaxMin(lista)#Se usa la función calculadoraMaxMin para la lista creada
main()#Se ejecuta el programa

