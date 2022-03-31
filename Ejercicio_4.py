"""Ejercicio 4
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""

def ConvertirEspaciado(texto):#Creamos la funcion Convertir Espaciado con un string de entrada
    for i in texto:#Inicia el ciclo for
        print (i,end=" ")#Para cada ciclo se imprime el caracter que lo conforma, seguido de un espacio.
def main():#Se crea el programa principal con una función main
    ConvertirEspaciado("Hola ¿Cómo estás?")#Se usa la función ConvertirEspaciado para espaciar un texto
main()
