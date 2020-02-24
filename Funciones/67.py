#Ejercicios con funciones punto 67
#Javier Aponte 20172020036

def esNumero(caracter):
    if(caracter == '0' or caracter == '1' or caracter == '2' or caracter == '3' or caracter == '4' or caracter == '5' or caracter == '6' or caracter == '7' or caracter == '8' or caracter == '9'):
        return True
    return False


c = input("Ingrese el caracter que desea verificar \n")
if esNumero(c):
    print("El caracter ingresado es un numero")
else:
    print("El caracter ingresado no es un numero")