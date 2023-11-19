def Num_conso():
    for i in range(1, 101):
        print(i)

def Multi_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def Multi_5():
    for i in range(1, 101):
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)
def Multi_3_5():
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
        1. imprimir Numeros pór consola del 1 al 100 por consola 
        2. Multiplos de 3 cambiarlos por la palabra Fizz
        3. Multiplos de 5 cambiarlos por la palabra Buzz
        4. Multiplos de 3 y de 5 a la vez cambiarlos por la palabra FizzBuzz
        5. Todo lo anterior mencionado Junto en una Impresion
        6. Salir 
        
        Elige Una Opcion : '''

        opcion = input(menu)
        if opcion == '1':
            print(Num_conso())

        elif opcion =='2':
            print(Multi_3())

        elif opcion == '3':
            print(Multi_5())

        elif opcion == '4':
            print(Multi_3_5()) 
        
        elif opcion == '5':
            print(Todo_Junto()) 
            
        elif opcion == '6':
            break 

if __name__ == '__main__':
    main()


