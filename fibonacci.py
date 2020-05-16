def fib(num):
    
    if num == 0 or num == 1:
         return 1
    else:
        result = fib(num-1) + fib (num-2)
        return result

num = int(input('¿que numero quieres calcular con la secuencia de fibonacci?: '))

for i in range(num):
    print(f'El factorial de {i} es: {fib(i)}')

print(f'Resultado de factorial de {num} es: {fib(num)}')