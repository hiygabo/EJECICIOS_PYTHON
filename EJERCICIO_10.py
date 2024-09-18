#DADO UN LOTE DE N NUMEROS DETERMINAR CUANTOS NUMEROS PRIMOS EXISTEN EN EL LOTE+
n=int(input("Ingrese la cantidad de numeros que estaran en el lote: "))
lote=[]
primos=0
no_primo=0
for i in range (n):
    numero=int(input("Ingrese un numero:"))
    lote.append(numero)
for i in lote:
    if (i-1)%2==0:
        no_primo+=1
    else:
        primos+=1
print("Primos: ",primos)
        
    