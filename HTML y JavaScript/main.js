let numIni = document.getElementById("numInicial");
let numFin = document.getElementById("numFinal");
let multiploN1 = document.getElementById("Fizz");
let multiploN2 = document.getElementById("Buzz");
let boton = document.getElementById("botonMostrar");
boton.addEventListener("click", mostrarFizzBuzz);
let resultado = document.getElementById("resultado");

function mostrarFizzBuzz() {
    let mul1 = parseInt(multiploN1.value);
    let mul2 = parseInt(multiploN2.value);

    resultado.innerHTML = " ";
    resultado.innerHTML += "<hr />";

    for (let i = parseInt(numIni.value); i <= parseInt(numFin.value); i++) {
        if (esDivisible(i, mul1)) {
            resultado.innerHTML += "Fizz";
        }
        if (esDivisible(i, mul2)) {
            resultado.innerHTML += "Buzz";
        }

        if (!esDivisible(i, mul1) && !esDivisible(i, mul2)) {
            resultado.innerHTML += i;
        }
        resultado.innerHTML += "<br />";
    }
}

    function esDivisible(num, divisor) {
        if (num % divisor == 0) {
            return true;
        }
        else {
            return false;
        }
    }