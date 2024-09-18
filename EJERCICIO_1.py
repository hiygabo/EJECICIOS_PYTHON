#CONTAR CUANTAS VECES APARECE UNA LETRA EN UNA CADENA INGRESADA POR EL USUARIO

palabra = input("Ingrese la palabra: ")
letra = input("Ingrese la letra: ")

contador = 0
for i in palabra:
    if i == letra:
        contador += 1
print(f"La letra {letra} aparece {contador} veces en la palabra {palabra}")