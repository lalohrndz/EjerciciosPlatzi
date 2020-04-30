/*
------Funciones--------
Para definir una funcion se ocupa la palabra reservada 'function'
seguido del nombre de la misma, finalizando con parentesis y llaves

=======================================================================
Ej:

function saludo(){
    console.log('Hola mundo!')
}

    *Para poder utilizar una funcion se debde llamar, esto se hace
    con el nombre de la funcion, parentesis y en caso del uso de parametros
    también se deben de agregar.

Ej:

saludo()
=======================================================================

    *Si nos queremos referir a una variable globar dentro de una
     funcion debemos de referirnos a window.[nombre de variable]
*/

var nombre = 'Lalo', edad = 23

function imprimirEdad(){
    console.log(`${nombre} tiene ${edad} años.`)

}

imprimirEdad()

//================================================================

function imprimirEnMayuscula(n){
    n = n.toUpperCase()
    console.log('Ejemplo de nombre con metodo .toUpperCase()')
    console.log(`${n}`)

}

imprimirEnMayuscula(nombre)
//================================================================


/*
----------Objetos----------

Un objeto es una colección de datos relacionados
que generalmente consta de variables y funciones
que se denominan 'propiedades' y 'métodos' cuando
están dentro de objetos

Ej:

1)  var objeto = new object()
2)  var objeto = {}


Los objetos constan de una clave y un valor

Clave -> se ubica a la izquierda, estos pueden ser strings o números
Valor -> se ubica a la derecha, estos pueden ser strings, numeros
*/

var persona = {
    nombre:'Pepe',
    apellido: 'Pastor',
    edad: 23
}