#GENERAR UNA SECUENCIA ARITMETICA DE N NUMEROS CON UNA RAZON DADA
n=int(input("Ingrese el termino que desea encontrar: "))
a1=int(input("Ingrese el primer termino: "))
d=int(input("Ingrese la razon: "))
an=a1+(n-1)*d
print(f"El termino {n} de la secuencia es: {an}")
