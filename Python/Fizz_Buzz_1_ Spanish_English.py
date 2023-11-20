#   1º Forma Corta Utilizando Funcion Corta Lambda 
#   1º Short Way Using  Lambda function
print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')


