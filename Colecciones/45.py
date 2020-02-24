#Ejercicios con Colecciones punto 45
#Javier Aponte 20172020036

print("Ingrese los numeros por favor \n")
lista = ()
while(True):
    aux1 = int(input())
    aux2 = (aux1,)
    lista += aux2
    r = int(input("Desea ingresar otro numero (1: si , 0: no \n)"))
    if r== 0:
        break

maximo =  lista[0]
x = 0
for i in range(0,len(lista)):
    if(lista[i] > maximo):
        maximo = lista[i]
        x = i
print("La lista ingresada es: ",lista,"\n")
print("Y el numero mayor esta en la posicion : ",x)