# Задача №9.
# Решение в группах По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input:       5 Output:    120

# def factorial(num):
#     fact = 1
#     while num > 1:
#         fact = fact * num
#         num = num-1
#     return fact
#
# num = int(input('Введите число: '))
# print (f'Факториал числа {num} равен {factorial(num)}')



# Задача №11. Решение в группах Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input:     5 Output:  6



def fibonaci(num):
    a, b, i = 0, 1, 1
    while a <= num:
        if num == a:
            return i
            break
        a, b, i = b, a+b, i+1

    else:
        return (-1)


num = int(input('Введите число: '))
print(fibonaci(num))