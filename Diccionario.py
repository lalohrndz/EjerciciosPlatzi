
def run():
    #Se rigen por un sistema de llave - valor, se crea con llaves
    calif = {}
    calif['saludo'] = 'Hola!'
    calif['despedida'] = 'Adios!'
    calif['Esta es la llave'] = 'Este es el valor'

    for key in calif:
        print(key)

    for value in calif:
        print(value)

    for key, value in calif.items():
        print('llave: {}, valor: {}'.format(key,value))

if __name__ == '__main__':
    print('''
    Diccionarios:
    Es similar a una lista, a diferencia que un diccionario se rige a partir de una llave y un valor.
    ''')
    run()