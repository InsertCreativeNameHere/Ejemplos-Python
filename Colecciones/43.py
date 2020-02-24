#Ejercicios con Colecciones punto 43
#Javier Aponte 20172020036

bandera = True
pares = ()
contador = 0
numero = 0
suma = 0
while(bandera):
    aux = (numero,)
    pares = pares + aux
    contador = contador + 1
    suma = suma + numero
    if numero == 0 :
        numero = 2
    else:
        numero = numero * 2
    if(contador == 20):
        bandera = False
print("La suma de los primeros 20 numeros pares es: ",suma,"\n")
print("Los primeros 20 numeros pares son: ",pares)