#ESCRIBIR UN PROGRAMA QUE VERIFIQUE SI UN NUMERO ES PERFECTO (ES DECIR SI SUS DIVISORES SUMAN EL MISMO NUMERO)
n=int(input("Ingrese un numero: "))
suma=0
if n <=0:
    print("El numero debe ser positivo")
else:
    for i in range (1,n):
        if n%i==0:
            suma+=i
    if suma == n:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")