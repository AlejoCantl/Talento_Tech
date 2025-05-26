let num1
let num2
let operacion =""

function realizarOperacion(num1, num2, operacion){
if(operacion === "1"){
    return num1+num2
}
else if(operacion === "2"){
    return num1-num2
}
else if(operacion === "3"){
    return num1*num2
}else if(operacion === "4"){
    if(num2===0){
        return "No se puede dividir, el divisior no puede ser 0";
    }
    else{
        return num1/num2
    }
}else{
    alert("Operacion invalida")
}
}

while(operacion !="0"){
    operacion = prompt(`Seleccione la operacion que desea realizar\n
        1. SUMA
        2. RESTA
        3. MULTIPLICACION
        4. DIVISION
        0. SALIR
        `)
    switch(operacion){
        case "1":
            num1= Number(prompt("Ingrese el primer numero"))
            num2= Number(prompt("Ingrese el segundo numero"))
            alert("La suma es "+realizarOperacion(num1, num2, "1"))
        break;
        case "2":
            num1= Number(prompt("Ingrese el primer numero"))
            num2= Number(prompt("Ingrese el segundo numero"))
            alert("La resta es "+realizarOperacion(num1, num2, "2"))
        break;
        case "3":
            num1= Number(prompt("Ingrese el primer numero"))
            num2= Number(prompt("Ingrese el segundo numero"))
            alert("La multiplicacion es "+realizarOperacion(num1, num2, "3"))
        break;
        case "4":
            num1= Number(prompt("Ingrese el dividendo"))
            num2= Number(prompt("Ingrese el divisior"))
            alert(`${num2!==0?"La division es "+realizarOperacion(num1,num2,"4"):realizarOperacion(num1, num2, "4")}`)
        break;
        case "0":
            alert("Programa terminado")
        break;
        default:
            alert("Opcion invalida")
    }
}
