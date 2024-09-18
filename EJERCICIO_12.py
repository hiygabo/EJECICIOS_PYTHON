#DADA UNA CADENA CAD QUE CONTIENE PALABREAS SEPARADAS ENTRE SI POR ESPACIOS EN BLANCO, 
# SE PIDE GENERAR UNA CADENA NUEVACAD QUE CONTENDRA LAS PALABRAS DE CAD, 
# CON LA DIFERENCIA DE QUE LAS PAALBRAS QUE TIENEN LONGITUD PAR LAS VAMOS A INVERTIR MEDIANTE SUS CARACTERES Y 
# LAS PALABRAS QUE TIENE LONGITUD IMPAR LAS VAMOS A ORDENAR MEDIANTE SUS CARATERES DE FORMA ASCENDENTE
#ADEMAS AL IGUAL QUE CAD, NUEVA CAD TIENE QUE TENER ESPACIOS EN BLANCO ENTRE CADA DOS PALABRAS
cad=input("Ingrese una cadena de palabras: ")
palabras=cad.split()
nueva_cad=[]
for palabra in palabras:
    if len(palabra)%2==0:
        nueva_cad.append(palabra[::-1])
        
    else:
        nueva_cad.append(''.join(sorted(palabra)))
        
nueva_cad= " " .join(nueva_cad)
print(nueva_cad)
        

        
        
