#Ejercicios con condicionales punto 20
#Javier Aponte 20172020036

r = int(input("Ingrese el primer numero por favor \n"))
s = int(input("Ingrese el segundo numero por favor \n"))

if(r*r == s):
    print("el segundo es el cuadrado exacto del primero")
elif(r*r > s):
    print("el segundo es menor que el cuadrado del primero")
else:
    print("el segundo es mayor que el cuadrado del primero")