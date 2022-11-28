# 2.	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# o	1, 4, 8, 7, 5 -> 8
# o	78, 55, 36, 90, 2 -> 90

max = int(input('Введите число'))
for i in range(4):
    a = int(input('Введите число'))
    if a > max:
        max = a
print(max)

# lst = []
# for i in range(5):
#     a = int(input('Введите число'))
#     lst.append(a)
# print(max(lst))
