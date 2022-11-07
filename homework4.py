# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def Prime(x):
    import math
    simple = True
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            simple = False
            break
        i += 1
    return(simple)

def Task1():
    N = int(input('Введите N: '))
    if Prime(N) == True and N == 1:
        print(f'{N} --> [1]')

    elif Prime(N) == True and N != 1:
        print(f'{N} --> [1, {N}]')

    else:
        nuturalNum = []
        N1 = N
        for i in range (2, (N1//2)+1):
            if Prime(i) == True:
                while N1 % i == 0:
                    nuturalNum.append(i)
                    N1 /= i
        print(f'{N} --> {nuturalNum}')


# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе. Выведите названия
# того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»


def Task2():
    data = open('ice_cream.txt', encoding='utf-8')
    iceCr = data.readlines()
    data.close()

    line1 = set(iceCr[0].replace('\n', '').split(', '))
    line2 = set(iceCr[1].replace('\n', '').split(', '))
    print(line1,'\n', line2)
    print(f'Закончилось: {line1.difference(line2)}')
        


# Задача 3. Выведите число π с заданной точностью.
# Точность вводится пользователем в виде натурального числа.
# 3 -> 3.142
# 5 -> 3.14159


def Task3():
    a = int(input('Задайте точность числа пи: '))
    import math
    print(f'{round(math.pi, a)}')


# Навигация по задачам в ДЗ №4
homework = True
while homework:
    homework = (input("Введите номер задачи (1, 2, 3), для выхода введите 'exit': "))
    if homework == 'exit':
        homework = not homework
    if homework == '1':
        Task1()
    elif homework == '2':
        Task2()
    elif homework == '3':
        Task3()
