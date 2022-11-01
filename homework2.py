# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Task1():
    import math

    numbers = float(input('Введите число N: '))

    numbers = abs(numbers)
    numbers = math.floor(numbers)
    fact = 1
    i = 1
    list = []

    if numbers > 1:
        while i <= numbers:
            fact *= i
            list.append(fact)
            i += 1
    else:
        print ('N должны быть не меньше 1')
    
    print(list)


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def Task2():  
    print('x | y | z | ¬(X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0,2):
                res = not (x and y) or z
                print(f'{x} | {y} | {z} | {int(res)}')


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def Task3():
    string_1 = input('Введите строку 1: ')
    string_2 = input('Введите строку 2: ')
    string_1 = set(string_1)

    for str in string_1:
        print(f'{str} - {string_2.count(str)}', end ='  ')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def Task4():
    import math
    N = float(input('Введите N: '))
    N = abs(N)
    N = math.floor(N)
    list = []

    for i in range(-N,N+1):
        list.append(i)
    list = list[-2:] + list[:-2]

    print(list)


# Навигация по задачам в ДЗ №2
numberTask = int(input("Введите номер задачи (1, 2, 3, 4): "))
if numberTask == 1:
    Task1()
elif numberTask == 2:
    Task2()
elif numberTask == 3:
    Task3()
elif numberTask == 4:
    Task4()
