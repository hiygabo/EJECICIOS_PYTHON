#LA CLAVE MURCIELAGO ES UNA SENCILLA CLAVE QUE COMO BOY SCOUT APRNDER DEBES
# ES FACIL DE REALIZAR POR SU VENTAJA DE CAMBIAR LAS LETRAS POR NUMEROS, TRABAJANDO CON LA SIGUIENE CONVERSION:
# M=0, U=1, R=2, C=3, I=4, E=5, L=6, A=7, G=8, O=9
# ESCRIBA UN PROGRAMA QUE DADA UNA CADENA DE TEXTO INGRESADA POR EL USUARIO
n=int(input())
for _ in range(n):
    texto = input("Ingrese el texto:")
    #for i in texto:
    texto = texto.replace("M","0")
    texto = texto.replace("U","1")
    texto = texto.replace("R","2")
    texto = texto.replace("C","3")
    texto = texto.replace("I","4")
    texto = texto.replace("E","5")
    texto = texto.replace("L","6")
    texto = texto.replace("A","7")
    texto = texto.replace("G","8")
    texto = texto.replace("O","9")
    print(texto) 