#DADA UNA CADENA DE ENTRADA, INDICAR SI LA MISMA ES PALINDROMA O NO
texto = input("Ingrese una palabra: ")
cadena = texto.replace(" ","").lower()

if cadena == cadena[::-1]:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")