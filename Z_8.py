"""
8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
number = int(input('Введите последовательность чисел(без разделителей): '))
mark = int(input('Укажите, количество какой цифры нужно посчитать: '))
count = 0

while number > 1:
    n = int(number % 10)
    number = int(number /10)
    if n == mark:
        count += 1
print(f'Число {mark} встретилось {count} раз.')