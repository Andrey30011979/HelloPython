# 3.	Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]


from random import randint

a= [1,2,2,2,2,3,1,4,5,5,7,6]

print(set(a))