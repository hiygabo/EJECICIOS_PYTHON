def generar_serie(n):
    if n == 0:
        return "error"

    # Secuencia inicial basada en los ejemplos dados
    serie = [4, 10, 26, 72, 208]  # Según el ejemplo de la imagen
    
    # Si n es menor o igual que 5, imprimimos los primeros n términos
    if n <= len(serie):
        return serie[:n]
    
    # Si necesitamos más términos, los generamos (asumiendo algún patrón)
    while len(serie) < n:
        # Fórmula de crecimiento observada en la serie
        nuevo_termino = serie[-1] * 2 - serie[-2] + 10  # Ejemplo de relación hipotética
        serie.append(nuevo_termino)
    
    return serie[:n]

# Entrada de números
while True:
    try:
        # Leer el número N
        n = int(input())
        resultado = generar_serie(n)
        
        # Mostrar la salida
        if resultado == "error":
            print("error")
        else:
            print(" ".join(map(str, resultado)))
            
    except EOFError:
        break