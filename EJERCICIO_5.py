# ESCRIBE UN PROGRAMA QUE CALCULE LA SUMA DE DIGITOS DE UN NUMERO ENTERO POSITIVO INGRESADO POR EL USUARIO
while True:
    try:
        numero = int(input("ingrese un numero entero positivo: "))
        if numero <=0:
            print("El numero ingresado no es positivo o es igual a 0")
            break
        suma = sum([int(x) for x in str(numero)])
        print (suma)
    except:
        break