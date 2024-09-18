n=int(input())
numero_original=n
contador_pasos=0
while True:
    n_str=str(n)
    
    suma=sum([int(x) for x in n_str])
    
    nuevo_numero= int(n_str[-1]+str(suma)[-1]) 
    contador_pasos+=1
    print(nuevo_numero)
    if nuevo_numero==numero_original:
        break
    
    n= nuevo_numero
print(f"El numero {numero_original} se repite en {contador_pasos} pasos")
    