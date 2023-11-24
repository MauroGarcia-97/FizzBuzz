let numeroInicial = document.getElementById("numeroInicial");
let numeroFinal = document.getElementById("numeroFinal");
let multiploNumero1 = document.getElementById("Fizz");
let multiploNumero2 = document.getElementById("Buzz");
let boton = document.getElementById("botonMostrar");
boton.addEventListener("click", mostrarFizzBuzz);
let resultado = document.getElementById("resultado");

function mostrarFizzBuzz() {
    let multiplo1 = parseInt(multiploNumero1.value);
    let multiplo2 = parseInt(multiploNumero2.value);

    resultado.innerHTML = " ";
    resultado.innerHTML += "<hr />";

    for (let i = parseInt(numeroInicial.value); i <= parseInt(numeroFinal.value); i++) {
        if (esDivisible(i, multiplo1)) {
            resultado.innerHTML += "Fizz";
        }
        if (esDivisible(i, multiplo2)) {
            resultado.innerHTML += "Buzz";
        }

        if (!esDivisible(i, multiplo1) && !esDivisible(i, multiplo2)) {
            resultado.innerHTML += i;
        }
        resultado.innerHTML += "<br />";
    }
}

    function esDivisible(numero, divisor) {
        if (numero % divisor == 0) {
            return true;
        }
        else {
            return false;
        }
    }