# Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
#  применив лямбды, filter, map, zip, enumerate, списочные выражения.
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# sp = [2, 3, 5, 9, 12, 16, 5]
# summ = 0
# for i in range(1, len(sp), 2):
#     summ += sp[i]
# print(f"{sp} сумма элементов на нечётных позициях: {summ}")

my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))