# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def Task1():
    import random
    number = str(random.randint(100,1000)) 
    print(f'Случайное число: {number}')

    number = [number, number*2, number*3]   # массив из строк
    number = [int(i) for i in number]       # преобразование элемента массива в числа

    print(f'{number[0]} + {number[1]} + {number[2]} = {sum(number)}')


# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите программу,
# которая определяет, есть в массиве последовательность из трёх элементов,
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def Task2():

    import random
    numbers = [random.randint(1,9) for i in range (15)]
    numbersStr = [str(i) for i in numbers]
    print(f'Случайный массив: {numbers}')

    n3 = int(input('Введите трехзначное число: '))
    if 99 < n3 < 1000:
        n3 = str(n3)
        result = 0
        numbersStr = ''.join(numbersStr)
        for i in range(0, 14):
            if numbersStr[i:i+3] == n3:
                print(f'{numbers} - {n3} -> да')
                result = 1
                break
        if result == 0:
            print(f'{numbers} - {n3} -> нет')
        
    else:
        print('Введенное число не трехзначное')



# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


# Можно, конечно, было сделать через встроеннуый метод, но решил заморочиться
def Task3():
    def Simple(x,y):
        result = True
        for i in range (2,x+1):
            if x % i == 0 and y % i == 0:
                result = False
                break
                return result
        return result

    nsd = []
    for i in range(2,12):
        for j in range(1,i):
            if j == 1:
                nsd.append(f'{j}/{i}')
            else:
                if Simple(j,i) == True:
                    nsd.append(f'{j}/{i}')
    print(nsd)
    

# Навигация по задачам в ДЗ №6
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
