def factorial(n):
    """
    Calcula el factorial del numero ingresado
    """
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('Escribe un entero: '))
print(f'El factorial de {n} es {factorial(n)}')