#DOKI RECIENTMENTE APRENDIO COMPOSICION Y DESCOMPOSICION DE DIGITOS, AHORA LE HAN DADO UNA TARA
#CONSITE EN: DADO DOS NUMEROS X Y Y CON IGUAL NUMERO DE DIGITOS
#GENRAR UN NUMERO Z INTERCAMBIANDO LOS DIGITOS DE X Y Y
#SIENDO EL MAYOR DIGITO QUIEN VA PRIMERO Y EL MENOR QUIEN VA DESPUES
def numero(x,y):
    x=str(x)
    y=str(y)
    z= ""
    for i in range(len(x)):
        digito_x = x[i]
        digito_y = y[i]
        if digito_x > digito_y:
            z+=digito_x + digito_y
        else:
            z+=digito_y + digito_x
    
    return z
    
    
n=int(input("ingrese el numero de casos de prueba: "))
for _ in range(n):
    x,y=map(int,input().split())
    if len(str(x))== len(str(y)):   
        resultado= numero(x,y)
        print(resultado)
    else:
        print("Los numeros no tienen el mismo numero de digitos")