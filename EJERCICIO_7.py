#ESCRIBE LOS NUMEROS PARES DE UNA LISTA DE NUMEROS ENTEROS INGRESADA POR EL USUARIO
n=int(input("Ingrese la cantidad de casos de prueba:"))
for _ in range (n):
    numeros = input("Ingrese los numeros separados por un espacio: ")
    lista = list(map(int, numeros.split(",")))
    for i in lista:
        if i%2==0:
            print(i)

