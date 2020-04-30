var persona = {
    nombre : 'lalo',
    apellido: 'pastor',
    edad: 23,
    peso: 85

}

console.log(`Al inicio del año ${persona.nombre} pesaba ${persona.peso} kg.`)

//funciones
const INCREMENTO_DE_PESO = 0.3
const DIAS_DEL_AÑO = 365
const AUMENTO_DE_PESO = persona => persona.peso += INCREMENTO_DE_PESO
const ADELGAZAR = persona => persona.peso -= INCREMENTO_DE_PESO

const META = persona.peso - 3
const COME_MUCHO = () => Math.random() < 0.3
const REALIZA_DEPORTE = () => Math.random() < 0.4

var dias = 0

while(persona.peso > META){
    if(COME_MUCHO()){
        //aumenta de peso
        AUMENTO_DE_PESO(persona)

    }if(REALIZA_DEPORTE()){
        //baja de peso
        ADELGAZAR(persona)
    }
    dias += 1
}

//misma aumento_de_peso funcion de arriba

//function aumentodepeso(persona){
//    return persona.peso +=200
//} 

for (var i = 1; i <= DIAS_DEL_AÑO; i++ ){
    var random = Math.random();
    
    if(random < 0.25){
        //aunmento de peso
        AUMENTO_DE_PESO(persona)
    }else if(random < 0.5){
        //adelgazar
        ADELGAZAR(persona)
    }else if(random < 0.75){
        
    }else{
    
    }
}
//tofixed() nos ayuda a manejar el número de decimales que aparecen
console.log(`Al final de ${dias} días, ${persona.nombre} pesa ${persona.peso.toFixed(1)} kg.`)
