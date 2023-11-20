def Numero_consola():
    for i in range(1, 101):
        print(i)

def Multiplo_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def Multiplo_5():
    for i in range(1, 101):
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)
def Multiplo_3_Y_5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)
def Todo_Junto():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
        elif i % 3 == 0:
                print('Fizz')
        elif i % 5 == 0:
                print('Buzz')
        else:
                print(i)
def main():
    while True:
        menu = '''          MENU
        1. Imprimir Numeros Pór Consola Del 1 Al 100  
        2. Multiplos De 3 Cambiarlos Por La Palabra " Fizz " 
        3. Multiplos De 5 cambiarlos Por La Palabra " Buzz "
        4. Multiplos De 3 & De 5 A La Vez Cambiarlos Por La Palabra " FizzBuzz "
        5. Todo Lo Anterior Mencionado Junto En Una Impresion
        6. Salir 
        
        Elige Una Opcion : '''

        opcion = input(menu)
        if opcion == '1':
            print(Numero_consola())

        elif opcion =='2':
            print(Multiplo_3())

        elif opcion == '3':
            print(Multiplo_5())

        elif opcion == '4':
            print(Multiplo_3_Y_5()) 

        elif opcion == '5':
            print(Todo_Junto()) 

        elif opcion == '6':
            break 

if __name__ == '__main__':
    main()

