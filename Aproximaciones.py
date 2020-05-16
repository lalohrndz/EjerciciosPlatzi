#Tomar la aproximación más cercana al resultado
numero = int(input('''Elige un numero:
'''))
#epsilon es que tan preciso se quiere llegar al resultado
epsilon = 0.01
paso = epsilon**2
resultado = 0.0

#la funcion abs regresa valore absolutos
#En el ciclo dentro de la funcion abs buscamos obtener el resultado al cuadrado menos el numero
#si en caso de no encontrar un resultado que sea menor o igual a epsilon y que también sea menor o igual al mismo numero
#se suma el resultado con el valor de la variable de 'paso'
while abs(resultado**2 - numero) >= epsilon and resultado <= numero:
    print(abs(resultado**2 - numero, resultado))
    resultado += paso

if abs(resultado**2 - numero) >= epsilon:
    print(f'No se encontro la raiz de {numero}')
else:
    print(f'La raiz cuadrada de {numero} es: {resultado}')