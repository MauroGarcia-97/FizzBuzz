/*   1º Forma Corta Utilizando Funcion Corta llamada Ternario */
/*   1º Short Way Using ternary function */
for (let i = 0; i < 100;) {
    console.log((++i % 3 ? '' : 'Fizz') + (i % 5 ? '' : 'Buzz') || i);
  }

