"""Ejercicio 1
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; 
pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
Además subraya el mensaje utilizando el carácter =."""

def EscribirCentrado(column,texto):#Defino la función con un número de columnas y un string de entrada
    espacio=int(column/2)-(int(len(texto)/2))#Defino la variable espacio, que indica el espacio antes de el texto
    for i in range(0,espacio):#Se imprimen los espacios antes del texto sin saltarse las líneas (end)
        print(end =" ")
    print(texto)#Se imprime el texto
    for k in range(0,espacio):#Se imprime los espacios antes de las líneas de subrayado
        print(end =" ")
    for j in range(0,len(texto)):#Se imprime el subrayado
        print(end ="=")
EscribirCentrado(80,"Hola mi nombre es Devi Orozco Fuentes, tengo 23 años")#Se llama a la función con los siguentes parámetros de entrada
