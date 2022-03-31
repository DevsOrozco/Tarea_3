"""Ejercicio 2
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""
def EsMultiplo(num1,num2):#Se define la función Es Múltiplo con dos numeros de entrada
    try:
        if num1%num2==0:#Si el módulo entre los dos números es 0, se imprime que son múltiplos
            print(f"El numero {num1} es multiplo de {num2}")
        else: 
            print(f"El numero {num1} no es multiplo de {num2}")#Caso contrario se imprime que no son múltiplos
    except Exception as e:#Se aplica la excepción e caso que los valores sean inválidos
        print("¡Error!Los valores ingresados no son enteros")
EsMultiplo(4,5)
EsMultiplo(20,5)