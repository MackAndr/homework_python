import matplotlib.pyplot as plt
from random import randint
import math 

# Задача 1. Постройте график функции
# 𝑓(𝑥) = 5𝑥^2 + 10𝑥 − 30
# По графику определите, при каких значения x значение функции отрицательно.

def task1():
    x = list(range(-50,50))

    f = list(5 * i * i + 10 * i - 30 for i in x)
    plt.plot(x, f)

    f1 = list(0 for i in x)
    plt.plot(x, f1)

    plt.show()
        
# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000
# рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и
# список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров,
# цены от 3 до 20 млн.

def task2():
    n = list(range(1,16))
    price = list(50000 for i in n)
    # hauseList - начальный список домов, hauseList1 - список стоимости кв.м каждого дома
    # hauseListFinish - искомый список домов
    hauseList = []
    hauseList1 = []
    hauseListFinish = []
    for i in range(15):
        
        h1 = randint(100, 300)
        h2 = randint(3000000, 20000000)
        h3 = math.floor(h2 / h1)
        h = (h1, h2, h3)
        hauseList1.append(h3)
        hauseList.append(h)
    print(f'Список всех домов(площадь, стоимость, стоимость кв.м) : {hauseList}')    
    print()

    for i in range(15):
        if hauseList1[i] < 50000:
            hauseListFinish.append(hauseList[i])
    print(f'Список домов(площадь, стоимость, стоимость кв.м) co стоимостью кв.м меньше 50000 :{hauseListFinish}')
    print()

    hauseListFinish.sort(key=lambda x: -x[0])
    print(f'Искомый список домов(площадь, стоимость, стоимость кв.м), отсортированный по площади: {hauseListFinish}')

    plt.plot(n, price)
    plt.plot(n, hauseList1)
    plt.show()    

# Навигация по задачам в ДЗ №6
homework = True
while homework:
    print()
    homework = (input("Введите номер задачи (1, 2), для выхода введите 'exit': "))
    print()
    if homework == 'exit':
        homework = not homework
    if homework == '1':
        task1()
        
    elif homework == '2':
        task2()
