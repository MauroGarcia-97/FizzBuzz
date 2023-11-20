#   2º Forma larga Utilizando Ciclos & Condicionales 
#   2º Long Form Using Loops & Conditionals.
for num in range(1,101):s
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 4 == 0:
        string = string + "Buzz"
    if num % 4 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
