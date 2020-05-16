print('''
Hola! Por favor elige un algoritmo a usar:
1)Enumeracion exhaustiva
2)Aproximacion de resultado
3)Busqueda binaria''')
eleccion = int(input(': '))

#Enumeracion exahustiva
def enumeracionExahustiva():
    print('''
    ======== Enumeración exahustiva ========
    ''')
    numero = int(input('Escoje un numero: '))
    respuesta = 0

    while respuesta**2 < numero:
        respuesta += 1
    
    if respuesta**2 == numero:
        print(f'La raiz de {numero} es: {respuesta}')
    else:
        print(f'No se encontró el resultado de {numero}')


#Aproximacion de resultado
def aproximacionDeResultado():
    print('''
    ======== Aproximacion de resultado ========
    ''')
    numero = int(input('Ingresa un numero: '))
    #epsilon marca la exactitud que dara el resultado aunmentando o disminuyendo los ceros despues del punto
    epsilon = 0.01
    #multiplicador para avanzar en la busqueda exacta del numero buscado
    paso = epsilon**2
    resultado = 0.0

    while abs(resultado**2 - numero) >= epsilon and resultado <= numero:
        resultado += paso
    
    if abs(resultado**2 - numero) >= epsilon:
        print(f'No se encontro resultado para {numero}')
    else:
        print(f'El resultado para {numero} es: {resultado}')

#Busqueda binaria
def busquedaBinaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

#if statements para correr las funciones
if eleccion == 1:
    enumeracionExahustiva()
elif eleccion == 2:
    aproximacionDeResultado()
elif eleccion == 3:
    busquedaBinaria()
else:
    print(f'el numero {eleccion} no se encuentra entre las opciones')
