# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	      1
# sp = [int(I) for I in input().split()]
# for element in sp:
#     if sp.count(element) == 1:
#         print(element)

# 2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	           5 4
# sp = [int(I) for I in input().split()]
# for i in range(len(sp)- 1):
#     if sp[i] < sp[i + 1]:
#         print(sp[i +1], end = " ")

# 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# Подсказка: можно использовать модуль datetime
# import time


# def mayrandom(x):
#    t = str(time.time())[-x:] 
#    print(t)


# mayrandom(3)

# 4.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Входные данные	Выходные данные
# 12
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка	              да
# sp = []
# count = 0
# a = input()
# for i in range(5):
#     s = input()
#     sp.append(s)

# for element in sp:
#     if a in element:
#         count +=1
# if count >= 1:
#     print('Да') 
# else: 
#     print ('Нет')     

# 5.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1

# sp = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find ="qwe"
# count = 0
# for i in range(len(sp)):
#     if sp[i] == find:
#         count +=1
#     if count == 2:
#         print(i)
#         break
# if count <= 1:
#     print(-1)        

# 1.	Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Входные данные	Выходные данные
# 1 5 2 2 2 4	     4
# sp = [1, 5, 2, 2, 2, 4]
# print(len(set(sp)))

# 2.	Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
# Входные данные	Выходные данные
# 1 3 2
# 4 3 2	             2 3
# sp1 = [1, 3, 2]
# sp2 = [4, 3, 2]
# print(*set(sp1) & set(sp2))# print(*set(sp1) | set(sp2))

# 3.	Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}
# Входные данные	Выходные данные
# Help me SOS
# 	.... . .-.. .--.
# -- .
# ... --- ...
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}
print(MORSE['A'])
s = "Help me SOS".upper().split()
for j in s:
    for i in j:
        if i in MORSE:
            print(MORSE[i], end=" ")
        else:
            print(i, end=" ")
    print()

