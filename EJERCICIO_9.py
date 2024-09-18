#DADO UN LOTE DE NUMEROS DETERMINAR CUANTOS NUMEROS PARES E IMPARES HAY EN EL LOTE
n=int(input("Ingrese la cantidad de numeros que estaran en el lote:"))
lote=[]
for i in range (n) :
    numero=int(input())
    lote.append(numero)
pares=0
impares=0
for i in lote:
    if i%2==0:
        pares+=1
    else:
        impares+=1
print("Pares: ",pares)
print("Impares: ",impares)
    
