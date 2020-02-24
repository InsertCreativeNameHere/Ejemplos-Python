#Ejercicios con Cadenas de caracteres punto 56
#Javier Aponte 20172020036

palabra = str(input("Ingrese la frase a la que le desea eliminar los espacios \n"))

sinEspa = ""

for i in palabra:
    if(i == ' '):
        continue
    sinEspa = sinEspa + str(i)
print("La fase ingresada es: ",palabra, "\n")
print("La fase ingresada sin espacios es: ",sinEspa, "\n")