#UN GRUPO DE AMIGOS LOS INSANOS DEBE ENTREGAR axbxc BANANAS AUN MONO DE MIERDA
#ANTES DE DARLE LAS BANANAS PUEDEN REALIZAR COMO MAXIMO 5 VECES LA SIGUIENTE OPERACION
#ESCOGER UNO DE LOS 3 NUMEROS
#SUMAR UNA UNIDAD AL NUMERO ESCOGIDO
def bananas(a,b,c,operaciones):
    for _ in range(operaciones):
        if a <=b and a<=c:
            a+=1
        elif b<=a and b<=c:
            b+=1
        else:
            c+=1
    return a*b*c

n = int(input("Ingrese el numero de casos de prueba: "))
for _ in range(n):
    a,b,c=map(int,input().split())
    operaciones = 5
    resultado = bananas(a,b,c,operaciones)
    print(resultado)