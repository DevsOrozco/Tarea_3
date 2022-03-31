"""Ejercicio 8
Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial."""

def factorial (n):#Se crea la funcion factorial, cuyo parámetro de entrada es un valor entero
    if n==0:#Caso 1: Factorial de 0 es 1
        return 1
    while n>0:
        if n==1:#Caso 2: Factorial de 1 es el mismo numero, al que le sumamos 1 para el siguiente ciclo.
            n+=1
            return 1
        elif n>1:#Caso 3: Factorial de numeros positivos distintos de 1, se le multiplica el número anterior al mismo
            return n*factorial(n-1)#la funcion se llama a si misma
        break

def main():#Función principal
    print("*Factorial*\n Por favor ingrese un número entero para calcular su factorial:")
    num=int(input())#Se almacena un valor enter en la variable num
    print(num,"! =",factorial(num))#Se imprime el resultado de la funcion factorial, asignandole el valor de num.

