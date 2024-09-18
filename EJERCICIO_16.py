#DADO UN LOTE DE N NUMEROS DETERMINAR CUALES DE ESTOS NUMEROS SON CAPICUAS
n=int(input("Ingrese la cantidad de casos de prueba: "))
lote =[]
for _ in range(n):
    numero = int(input("Ingrese un numero: "))
    lote.append(numero)
for i in lote: #[123, 121, 12321]
    if i == int(str(i)[::-1]):
        print(i) 