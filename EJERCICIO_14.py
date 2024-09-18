#GABRIEL EL INSANO, ESTA INTENTANDO CREAR UNA CONTRASEÑA EN EL JUEZ PATITO,PERO NO PUEDE CRAR LA CUENTA,YA QUE EL JUEZ
#LE DICE QUE SU CONTRASEÑA ES MUY DEBIL
#LA CONTRASEÑA DEBE CUMPLIR CON LOS SIGUIENTES REQUISITOS:
#1. MINIMO 4 NUMEROS
#2. MINIMO 2 LETRAS MAYUSCULAS
#3 MINIMO 2 LETRAS MINUSCULAS
#4 MINIMO 1 CARACTER ESPECIAL
import string
n=int(input())
for _ in range(n):
    contraseña=input("Ingrese la contraseña: ")
    numeros= sum(1 for c in contraseña if c.isdigit())
    mayusculas = sum(1 for c in contraseña if c.isupper())
    minusculas = sum(1 for c in contraseña if c.islower())
    especiales= sum(1 for c in contraseña if c in string.punctuation)
    
    if len(contraseña)<9:
        print("Debil")
    
    elif numeros>=4 and mayusculas>=2 and minusculas>=2 and especiales>=1:
        print("Segura")
    else:
        print("Debil")
        
