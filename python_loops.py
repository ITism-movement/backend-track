"""Цикл while"""
"""Цикл while выполняется до тех пор, пока заданное условие истинно."""
"""while условие:
    тело цикла"""
# Пример цикла while
# i = 10
# while i >= 5:
#     print('Our number is {b}. {a}'.format(a = i, b = 'test'))
#     i -= 1
# else:
#     print('It is done')

# бесконечный цикл while

# while True:
#     print('Oops')

# num_1 = 10
# while num_1 >= 5:
#     print('Our number is {}'.format(num_1))

"""Цикл for"""
"""Цикл for используется для итерации по последовательностям (спискам, строкам, словарям и т.д.) или любым итерируемым объектам."""
"""for переменная in последовательность:
    тело цикла"""

# start = 100
# stop = 20
# step =-2
# for i in range(start, stop, step):
#     print('Our number is {}'.format(i))

# break используется для немедленного выхода из цикла.

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue пропускает оставшуюся часть текущей итерации и переходит к следующей.

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# бесконечный цикл while

# while True:
#     print('Oops')
#
# num_1 = 10
# while num_1 >= 5:
#     print('Our number is {}'.format(num_1))

# выход из бесконечного цикла

# user_list = list()
# while True:
#     user_input = input('Введите слово для списка: ')
#     if user_input == 'stop':
#         print(user_list)
#         break
#     else:
#         user_list.append(user_input)
#         print(user_list)

"""Вложенные циклы
Циклы могут быть вложенными: один цикл находится внутри другого."""

# for i_num in range(1, 10):
#     for j_num in range(1, i_num + 1):
#         print('{} * {} = {}'.format(i_num, j_num, i_num*j_num))

# first_list = [43, 56, 675, 3455]
# second_list = [35, 675, 767, 3455]
#
# count_map = dict()
#
# for i_elem in first_list:
#    count_map[i_elem] = 0
#    for j_elem in second_list:
#         if i_elem < j_elem:
#             count_map[i_elem] += 1
#
# print(count_map)





"""Comprehensions для генерации коллекций
Comprehensions позволяют создавать списки, множества, словари и генераторы в лаконичной форме."""

# Списковое включение (List Comprehension):Словари (Dict Comprehension):

# squares = [x**2 for x in range(1, 6, 2)]
# print(squares)
#
# #Множества (Set Comprehension):
# unique = {x % 3 for x in range(10)}
# print(unique)
#
# #Словари (Dict Comprehension):
# squares_dict = {x:y**2 for x in range(25) for y in range(5)}
# l = [(x, y**2) for x in range(25) for y in range(5)]
# print(squares_dict)
# print(l)
#
# #Comprehensions поддерживают условия:
# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)
# even_squares = tuple(x**2 for x in range(10) if x % 2 == 0)
# print(even_squares)