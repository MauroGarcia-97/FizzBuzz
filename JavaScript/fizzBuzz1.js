/*   1º Forma Corta Utilizando Funcion Corta llamada Ternario */
for (let i = 0; i < 100;) {
    console.log((++i % 3 ? '' : 'Fizz') + (i % 5 ? '' : 'Buzz') || i);
  }

