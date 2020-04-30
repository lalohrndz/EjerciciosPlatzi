//CONDICIONALES Y COMPARACIONES

var x = 4, y = '4'
var lalo = {
    nombre : 'lalo',
    apellido : 'pastor',
    edad: 20,
    ingeniero : false,
    cocinero: false,
    dj: false,
    drone: true
}

var pepe = {
    nombre : 'pepe',
    apellido : 'grillo',
    edad: 17,
    ingeniero : false,
    cocinero: true,
    dj: false,
    drone: true
}

function profesiones(persona){
    console.log(`${persona.nombre} es:`)
    if(persona.ingeniero){
        console.log('Ingeniero')
    }else if(persona.cocinero){
        console.log('Cocinero')
    }else if(persona.dj){
        console.log('Dj')
    }else if(persona.drone){
        console.log('Piloto de Drones')
    }
}   

const MAYORIA_DE_EDAD = 18
 //arrow function => / funcion anonima const
const esMayorDeEdad = persona => {
    return persona.edad >= MAYORIA_DE_EDAD
}



function mayorDeEdad(persona){
    var Edadpersona = persona.edad
    if(esMayorDeEdad(persona)){
        console.log(`${persona.nombre} es mayor de edad por sus ${persona.edad} años`)
    }else{
        console.log(`${persona.nombre} es menor de edad por sus ${persona.edad} años`)
    }
}

const menorDeEdad = persona =>{
    return persona.edad <= MAYORIA_DE_EDAD
}

const permitirAcceso = persona =>{
    if(esMayorDeEdad(persona)){
        console.log('Acceso permitido')
    }
    if(menorDeEdad(persona)){
        console.log('Acceso denegado')
    }
}