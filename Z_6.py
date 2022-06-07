"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано. Если за 10 попыток
число не отгадано, вывести ответ.
"""
import random
random_number = random.randint(0, 100)
count = 10
print(random_number, type(random_number))

while count > 0:
    user_number = int(input('Введите число: '))
    if random_number != user_number:
        count -= 1
        if random_number - user_number > 0:
            print(f'Не угадали. Загаданное число, больше. Количество попыток: {count}')
        else:
            print(f'Не угадали. Загаданное число, меньше. Количество попыток: {count}')
    else:
        print(f'Вы победили. Загаданное число: {random_number}')
        break
else:
    print(f'Вы проиграли. Загаданное число: {random_number}')