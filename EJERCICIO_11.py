#DADO UN LOTE DE N NUMEROS DETERMINAR LOS DIVISORES DE CADA NUMERO
n=int(input("Ingrese la cantidad de numeros que estaran en el lote:"))
lote=[]
for i in range (n):
    numero=int(input("Ingrese un numero: ")) #1,2,3,4,5
    lote.append(numero) #[1,2,3,4,5]
for numero in lote:
    divisor=[]
    for i in range(1,numero+1):
        if numero % i ==0:
            divisor.append(i)
    print(f"Los divisores de {numero} son {divisor}")
        
    
    


