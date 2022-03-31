"""Ejercicio 12
Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: 
numerador y denominador. """
def Leer_fraccion(a,b):
    return Simplificar_fraccion(a,b)
def Escribir_fraccion(a,b):
    if b!=0:
        return a,b
    if b==1:
        return a
def Calcular_mcd(a,b):
        if a%b==0:
            return b
        elif a%b!=0:
            return Calcular_mcd(b,a%b)
        elif a<b:
            Calcular_mcd(b,a)
        elif b==0:
            return a
def Simplificar_fraccion(a,b):
    simp_a=int(a/Calcular_mcd(a,b))
    simp_b=int(b/Calcular_mcd(a,b))
    return simp_a,simp_b
def Sumar_fracciones(a,b,c,d):
    den=b*d
    num=(a*d)+(b*c)
    return Simplificar_fraccion(num,den)
def Restar_fracciones(a,b,c,d):
    den=b*d
    num=(a*d)-(b*c)
    return Simplificar_fraccion(num,den)
def Multiplicar_fracciones(a,b,c,d):
    num=a*c
    den=b*d
    return Simplificar_fraccion(num,den)
def Dividir_fracciones(a,b,c,d):
    num=a*d
    den=b*c
    return Simplificar_fraccion(num,den)
def main():
    print("*Operaciones con Fracciones*\n Por favor ingresa las fracciones que deseas operar:")
    n1=int(input("Numerador 1: ")); d1=int(input("Denominador 1: "))
    n2=int(input("Numerador 2: ")); d2=int(input("Denominador 2: "))
    a,b=(Escribir_fraccion(n1,d1))
    c,d=(Escribir_fraccion(n2,d2))
    print("Fraccion 1:",Leer_fraccion(a,b))
    print("Fraccion 2:",Leer_fraccion(c,d))
    n1=0
    while n1!=5:
        print("Seleccione el número según la operación que desea realizar:")
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
        n1=int(input())
        if n1==1:print("Suma:",Sumar_fracciones(a,b,c,d))
        elif n1==2:print("Resta",Restar_fracciones(a,b,c,d))
        elif n1==3:print("Multiplicacion",Multiplicar_fracciones(a,b,c,d))
        elif n1==4:print("Division",Dividir_fracciones(a,b,c,d))
        elif n1==5:print("Salir")
        else: print("El número que ingresó no está en el menú")
    print("Fin de las operaciones")
    #print(Simplificar_fraccion(1,39))
    #print(Sumar_fracciones(4,3,2,5))
    #print(Restar_fracciones(4,3,2,5))
    #print(Multiplicar_fracciones(4,3,2,5))
    #print(Dividir_fracciones(4,3,2,5))
main()
