let initialNumber = document.getElementById("initialNumber");
let finalNumber = document.getElementById("finalNumber");
let multipleNumber1 = document.getElementById("Fizz");
let multipleNumber2 = document.getElementById("Buzz");
let button = document.getElementById("showButton");
button.addEventListener("click", showFizzBuzz);
let result = document.getElementById("result");

function showFizzBuzz() {
    let multiple1 = parseInt(multipleNumber1.value);
    let multiple2 = parseInt(multipleNumber2.value);

    result.innerHTML = " ";
    result.innerHTML += "<hr />";

    for (let i = parseInt(initialNumber.value); i <= parseInt(finalNumber.value); i++) {
        if (isDivisible(i, multiple1)) {
            result.innerHTML += "Fizz";
        }
        if (isDivisible(i, multiple2)) {
            result.innerHTML += "Buzz";
        }

        if (!isDivisible(i, multiple1) && !isDivisible(i, multiple2)) {
            result.innerHTML += i;
        }
        result.innerHTML += "<br />";
    }
}

    function isDivisible(number, divider) {
        if (number % divider == 0) {
            return true;
        }
        else {
            return false;
        }
    }