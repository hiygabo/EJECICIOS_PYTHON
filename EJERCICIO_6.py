#ESCRIBE UN PROGRAMA QUE INVIERTA UNA CADENA DE TEXTO INGRESADA POR EL USUARIO
n=int(input())
for _ in range(n):
        palabra = input("Ingrese una palabra:")
        print(palabra[::-1])
    
