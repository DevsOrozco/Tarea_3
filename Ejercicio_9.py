"""Ejercicio 9
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD."""

def Metodo_Euclides(n1,n2):#Creo la función Método Euclides
    if n1>n2:#Si el número 1 es mayor al número 2
        while n1%n2!=0:#Creo el método while
            r=n1%n2#Se almacena el residuo
            n1=n2#Se cambia el dividendo por el divisior
            n2=r#Se cambia el divisor por el residuo
        return n2#Retorna el divisor previo
    elif n1<n2:#Si el número 1 es mayor al número 2
        while n2%n1!=0:#Creo el método while
            r=n2%n1#Se almacena el residuo
            n2=n1#Se cambia el dividendo por el divisior
            n1=r#Se cambia el divisor por el residuo
        return n1#Se retorna el divisior previo
    else:
        return n2#Si ambos números son iguales, el mcd es el mismo número

def main():#Función principal
    print("*MCD*\n Por favor ingrese dos números enteros para calcular su MCD:")
    n1=int(input());n2=int(input())
    print("MCD:",Metodo_Euclides(n1,n2))
    #print("MCD:",Metodo_Euclides(60,48))
    #print("MCD:",Metodo_Euclides(24,16))
    #print("MCD:",Metodo_Euclides(30,78))
    #print("MCD:",Metodo_Euclides(75,120))
    
main()