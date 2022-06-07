"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа
'0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""
while True:
    mark = input('Введите операцию, которую хотите совершить: "+, -, *, /" или 0 (если хотите выйти из программы): ')
    if mark != '+' and mark != '-' and mark != '*' and mark != '/' and mark != '0':
        mark = input('Введено некорректное значение оператора. Выберите операцию из предложенных: ')
    if mark == '0':
        print('Программа завершена')
        break

    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    if mark == '+':
        result = a + b
        print(f'{a} + {b} = {result}')
    elif mark == '-':
        result = a - b
        print(f'{a} - {b} = {result}')
    elif mark == '*':
        result = a * b
        print(f'{a} * {b} = {result}')
    elif mark == '/':
        try:
            result = a / b
            print(f'{a} / {b} = {result}')
        except ZeroDivisionError:
            b = int(input('На "0" делить нельзя. Введите иной делитель: '))
            result = a / b
            print(f'{a} / {b} = {result}')


