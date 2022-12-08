# Задача 1. В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random

def Task1():
    

    count_of_goups = int(input('Введите число групп '))
    all_points = [0] * count_of_goups

    for group in range(len(all_points)):
        all_points[group] = list(random.randint(1,10) for student in range(random.randint(20,30)))


    mild_points = []

    for points_of_group in all_points:
        mild = 0
        for point in points_of_group:
            mild += point
        mild_points.append(round(mild/len(points_of_group), 2))

    for points_of_group in all_points:
        print(points_of_group)

    print(mild_points)

    max_point = max(mild_points)
    number_of_group = mild_points.index(max_point)

    print(f'Максимальный бал по 10-и бальной шкале {max_point} у группы {number_of_group + 1}')
    


# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def Task2():
    n = random.randint(3,6)
    matrix = [0] * n

    for i in range(n):
        matrix[i] = list(random.randint(1,9) for j in range(n))
    
    for i in matrix:
        print(i)

    summ_of_diagonal = 0
    print('Сумма главной диагонали ', end=' (')
    for i in range(n):
        print(matrix[i][i], end=' ')
        summ_of_diagonal += matrix[i][i]
    print(f') равна {summ_of_diagonal}')
    # print(summ_of_diagonal)

    summ_of_rows = []
    for i in matrix:
        summ_of_rows.append(sum(i))
    
    print(f'Суммы строк: {summ_of_rows}')
    print('строки, в которых сумма элементов больше, чем в главной диагонали: ', end=' ')
    count = 0
    for i in range(len(summ_of_rows)):
        if summ_of_rows[i] > summ_of_diagonal:
            print(f'{i+1}', end='  ')
            count += 1
    if count == 0:
        print('таких строк нет')


# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

def Task3():
    def find_data(days):
        for month_number in range(len(matrix)):
            days_in_month = len(matrix[month_number])
            if days_in_month >= days:
                return (month_number, days)
            else:
                days -= days_in_month

    period = 7
    monthsInfo = [('мая', 31), ('июня', 30), ('августа', 31), ('сентября', 30)]
    size = len(monthsInfo)
    matrix = [0] * size

    for i in range(size):
        matrix[i] = list(random.randint(10, 30) for c in range(monthsInfo[i][1]))

    print('матрица-календарь')
    for i in matrix:
        print(i)
    print()

    matrix_in_row = []
    for row_matrix in matrix:
        for el in row_matrix:
            matrix_in_row.append(el)

    mean_temp = []
    for i in range(len(matrix_in_row) - period + 1):
        mean_temp.append(round(sum(matrix_in_row[i:i+period])/period, 2))

    max_el = max(mean_temp)
    index_max_el = mean_temp.index(max_el)
    print(f'средняя максимальная температура за {period}-период {max_el}')
    dateStart = find_data(index_max_el + 1)
    dateFinish = find_data(index_max_el + period)
    print(f'Самый теплый {period}-дневной период')
    print(f'{dateStart[1]} {monthsInfo[dateStart[0]][0]} - {dateFinish[1]} {monthsInfo[dateFinish[0]][0]}')
    print()
    min_el = min(mean_temp)
    index_min_el = mean_temp.index(min_el)
    print(f'средняя минимальнаяя температура за {period}-период {min_el}')
    dateStart2 = find_data(index_min_el + 1)
    dateFinish2 = find_data(index_min_el + period)
    print(f'Самый холодный {period}-дневной период')
    print(f'{dateStart2[1]} {monthsInfo[dateStart2[0]][0]} - {dateFinish2[1]} {monthsInfo[dateFinish2[0]][0]}')

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
