#Ejercicios con Recursividad punto 77
#Javier Aponte 20172020036


def contarDigitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return  1 +contarDigitos(int(numero/10))



c = int(input("Ingrese un numero \n"))

print("El numero de digitos del numero ingresado es: ",contarDigitos(c))