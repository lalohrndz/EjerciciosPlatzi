'''
se crea una nueva entrada en la pila de llamadas del intérprete. 
Ésta tiene un espacio limitado por lo que puede llegar un punto 
en el que si se hacen demasiadas se sature y se produzca un error. 
A este error se le denomina Desbordamiento de pila o Stack Overflow.
'''

def recursion(num):
    if num == 0:
        return 1
    
    return num * recursion(num - 1)

if __name__ == "__main__":
    num = int(input('''
    EJERCICIO CON NUMEROS FACTORIALES
    - INGRES EL NUMERO AL CUAL QUIERE ENCONTRAR EL FACTORIAL
    => '''))
    result = recursion(num)
    print (result)