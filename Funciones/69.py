#Ejercicios con funciones punto 69
#Javier Aponte 20172020036

def descuento(precio,cantidad):
    
    if(cantidad > 12):
        return precio * 0.1
    elif(cantidad > 6):
        return precio * 0.04
    else:
        return 0


p = float(input("Ingrese el precio del producto \n"))
cant = int(input("Ingrese la cantidad \n"))

des = descuento(p,cant)

print("El descuento para la compra es: ",des)

