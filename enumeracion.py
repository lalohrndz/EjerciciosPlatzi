#Enumeración exhaustiva
numero = int(input('''Escoje un entero:
'''))
respuesta = 0
while respuesta**2 < numero:
    print(f'el estatus de la respuesta es: {respuesta}')
    respuesta += 1

if respuesta**2 == numero:
    print(f'La raiz cuadrada de {numero} es {respuesta}')
else:
    print(f'{numero} no tiene una raiz cuadrada exacta')