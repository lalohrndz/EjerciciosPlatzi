#Scope o alcance
un_arg = 1

#Esta es la primera funcion a ejecutar y toma como parametros a la primer variable un_arg y a la funcion cualquier_func
#Al ejecutar la funcion se declara otra funcion que toma el valor de la variable, la multiplica
#y regresa el resultado a la funcion que lo invoco, en este caso a la linea 21
def func_uno(un_arg, cualquier_func):
    def func_dos(un_arg): 
        return un_arg*2

    valor = func_dos(un_arg) #la variable valor guarda el resultado de la funcion que se invoca de la linea 8
                             #guarda el resultado del retorno en la lina 9
    return cualquier_func(valor) #invoca a la funcion cualquier_func metiendo el valor de la variable valor
                                 #la funcion realiza la operacion de la linea 17 y regresa el valor a la linea 21

def cualquier_func(cualquier_arg):
    return cualquier_arg + 5

#Empezamos por llamar a la funcion func_uno que toma como argunmentos un_arg y cualquier_func
#El código empieza aqui y lo imprime en la misma linea:
print(func_uno(un_arg,cualquier_func))