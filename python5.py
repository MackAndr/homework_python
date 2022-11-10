# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


def Task1():
    import random
    numbers = [random.randint(1,10) for i in range (6)]

    result = list(filter(lambda x: x > 5, numbers))
    print(f'{numbers} -> {result}')

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


def Task2():
    import random
    numbers = [random.randint(1,99) for i in range (40)]
    print(f'Начальный список {numbers}')

    count = random.randint(0, 40)
    print(f'Cлучайный элемент: Numbers[{count}] = {numbers[count]}')
    numbers = numbers[count:40]
    print(f'Промежуточный список {numbers}')
    result = [numbers[0]]

    
    while count < 40:
        count = random.randint(count+1, 40)
        if numbers[40-count] > result[-1]:
            result.append(numbers[40-count])
    print(f'Искомый список: {result}')


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего
# совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def Task3():
    import random
    numbers = [random.randint(1,10) for i in range (8)]
    numbers.sort()
    

    new_numbers = set(numbers)
    new_numbers = list(new_numbers)
    

    copy_list = list(filter(lambda x: x > 1, [numbers.count(i) for i in new_numbers]))
    sum = 0
    for i in copy_list:
        sum += i
    print(f'{numbers} => {sum} элемента совпадают')

    print(new_numbers)


# Навигация по задачам в ДЗ №5
homework = True
while homework:
    print()
    homework = (input("Введите номер задачи (1, 2, 3), для выхода введите 'exit': "))
    print()
    if homework == 'exit':
        homework = not homework
    if homework == '1':
        Task1()
        
    elif homework == '2':
        Task2()
        
    elif homework == '3':
        Task3()
