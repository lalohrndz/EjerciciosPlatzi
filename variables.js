var nombre = 'lalo'
var apellido = 'pastor'

console.log(nombre)
console.log(apellido)
console.log(nombreCompleto)

var primeraLetraDelNombre = nombre.charAt(0)
var ultimaLetraDelNombre = nombre.charAt(nombre.length -1)
var cantidadDeLetras = nombre.length

//Esto es una interporación de texto, se declara con la comilla simple invertida
var nombreCompleto = `${nombre} ${apellido}`

//para acceder a un substring (una parte de un string)
var str = nombre.charAt(1) + nombre.charAt(2)
//indicas el inicio y el fin en el index del string que vas a recorrer
var strDos = nombre.substr(1,2)