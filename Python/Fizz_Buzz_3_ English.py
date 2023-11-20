def Number_console():
    for i in range(1, 101):
        print(i)

def Multiple_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def Multiple_5():
    for i in range(1, 101):
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)
def Multiple_3_Y_5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)
def All_Together():
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
       	1. Print Numbers Per Console From 1 To 100 Per Console
        2. Multiples Of 3 Change Them For The Word " Fizz " 
        3. Multiples Of 5 Change Them For The Word " Buzz " 
        4. Multiples Of 3 And 5 At The Same Time Change Them To The Word " FizzBuzz "
        5. All Of The Above Together In One Print
        6. Exit
        
        Choose An Option:'''

        option = input(menu)
        if option == '1':
            print(Number_console())

        elif option =='2':
            print(Multiple_3())

        elif option == '3':
            print(Multiple_5())

        elif option == '4':
            print(Multiple_3_Y_5()) 

        elif option == '5':
            print(All_Together()) 

        elif option == '6':
            break 

if __name__ == '__main__':
    main()

