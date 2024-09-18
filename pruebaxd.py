def factorial(n):
    if n < 0:
        return "Factorial no definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Calcular y mostrar el factorial de 10
print(f"Factorial de 10 es {factorial(10)}")