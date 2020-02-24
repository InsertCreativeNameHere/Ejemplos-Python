#Ejercicios con Cadenas de caracteres punto 61
#Javier Aponte 20172020036

palabra = str(input("Ingrese la frase que quiere pasar al reves \n"))

reves = ""

for i in range(len(palabra)-1,-1,-1):
    reves = reves + str(palabra[i])

print("La cadena que escribo al reves es: ",reves)