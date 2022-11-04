# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

# Вариант через рекурсию
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def Task1():
#     list = []
#     N = int(input('Введите N: '))
#     for e in range(1, N+1):
#         list.append(fib(e))

#     data = open ('fib.txt', 'w')
#     for i in range (N):
#         data.writelines(str(list[i]) + '\n')
#     data.close()


def Task1():
    N1 = 0
    N2 = 1
    count = int(input("Введите N: "))
    data = open('fib.txt', 'w')
    for i in range(count):
        data.writelines(str(N1) + '\n')
        (N1, N2) = (N2, N1 + N2)
    print('Файл "fib.txt" создан/перезаписан')
    data.close()


# Задача 2. В файле находятся названия фруктов. Выведите все фрукты,
#  названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.


def Task2():
    with open('fruits.txt', encoding='utf-8') as data:
        fruits = data.readlines()
        letter = input('Введите букву: ')
        for line in fruits:
            if line[0].lower() == letter.lower():
                print(line)
    data.close()


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

def Task3():
    dictionary = \
        {
            'привет' : 'ку',
            'как тебя зовут?' : 'Игнат',
            'как тебя зовут' : 'Игнат',
            'как дела?' : 'да вот, в чате типа сижу',
            'как дела' : 'да вот, в чате типа сижу',
            'кто ты?' : 'бот',
            'кто ты' : 'бот',
            'что нового?' : 'ничего =(',
            'пока' : 'я здесь, пока ты не напишешь выход',
            'выход' : 'всего доброго!'
        }

    dialog = True
    while dialog:
        question = input('Я: ')
        question[0].lower()
        if question == 'выход':
            dialog = not dialog
        if question in dictionary.keys():
            print('Бот:', dictionary[question])
        else:
            print('Бот: неизвестная команда')

# Навигация по задачам в ДЗ №3
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
