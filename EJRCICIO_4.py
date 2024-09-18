#ESCRIBE UN PROGRAMA QUE REMPLACE TODAS LAS OCURRENCIAS DE UNA SUBCADENA EN UN TEXTO DADO POR OTRA SUBCADENA INGRESADA POR EL USUARIO

texto = input("Ingrese el texto: ")
subcadena = input("Ingrese la subcadena a reemplazar: ")
subcadena_de_reemplazo= input("Ingrese la subcadena de reemplazo: ")
texto = texto.replace(subcadena, subcadena_de_reemplazo)
print(texto)
