#Ejercicios con Recursividad punto 79
#Javier Aponte 20172020036


def sumNumeros(cantidad):
    if(cantidad == 1):
        return 1
    return cantidad + sumNumeros(cantidad-1)


num =  int(input("Ingrese hasta que numero se quiere que se haga la suma: \n"))
print("La suma de los primeros ",num, " es:", sumNumeros(num))