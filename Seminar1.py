# Задача №1
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами. Input: n = 700 m = 750 Output: 2

# from math import ceil
#
# day_trip = input('Введите, сколько километров машина проезжает за день: ')
# common_path = input('Введите, сколько километров машина должна проехать: ')
#
# print ('Машина проедет ' + common_path + ' километров за ' + str(ceil(int(common_path)/int(day_trip))) + ' дней')

# Задача №3
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# from math import ceil
#
# first_grade_students = int(input('Введите число учащихся в первом классе: '))
# second_grade_students = int(input('Введите число учащихся во втором классе: '))
# third_grade_students = int(input('Введите число учащихся в третьем классе: '))
#
# print('Необходимо приобрести ' + str(ceil(first_grade_students/2) + ceil(second_grade_students/2) + ceil(third_grade_students/2)) + ' парт')

# Задача №5
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6


# account_number = int(input('Введите номер вагона от головы состава: '))
# serial_number = int(input('Введите порядковый номер вагона: '))
# print('Нумерация поезда с головы состава, для определения количества вагонов поезда необходимы дополнительные сведения' if account_number==serial_number
#       else 'В электричке ' + str(account_number + serial_number - 1) + ' вагонов')



# Задача №7. Решение в группах Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016 Output: YES


year = int(input('Введите год: '))
print('YES' if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 'NO')