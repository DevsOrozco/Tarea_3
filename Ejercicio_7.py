"""Ejercicio 7
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo."""
def Login (nombre_usuario,contraseña,n):#Se crea la función Login
    if nombre_usuario =="usuario1" and contraseña== "asdasd": #Si el nombre de usuario y contraseña coinciden
        n=0
        return True#Devuelev verdadero
    else:
        n+=1
        return False#Caso contrario devuelve falso

def main():#Se crea el programa principal
    global n#Se declara la variable global n
    n=0#Al principio hay 0 intentos
    while n<3:#Mientras los intentos sean menor a 3:
        usuario=str(input("Por favor ingrese su nombre de usuario: "))#Se solicita el usuario
        clave=str(input("Por favor ingrese su clave: "))#Se solicita la contraseña
        if n<3 and Login(usuario,clave,n)==True:#Se llama a la función Login para comprobar los datos
            print("Acceso correcto")#Si es verdadero, se accede correctamente
            pass
        else:
            print("El usuario o la clave son incorrectos")#Si es falso, se indica que el usuario o clave son incorrectos
            n+=1
    if n==3:
        print("Ha superado el número de intentos, vuelva más tarde")#Si se supera el número de intentos, se indica al usuario que intente ingresar más tarde y se termina el programa
main()