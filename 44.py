def summ():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите второе число: '))
    return num1+num2

command = input('Введите команду: ')
while command!="выход":
    if command == "+":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1+num2)
    elif command == "-":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1-num2)
    elif command == "*":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1*num2)
    elif command == "/":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1/num2)
    command = input('Введите команду: ')
print("Калькулятор выключен")