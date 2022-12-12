# 3.	Задайте два числа. Напишите программу, которая найдёт НОК
#  (наименьшее общее  кратное) этих двух чисел.

a = int(input('Задайте число: '))
b = int(input('Задайте второе число: '))
if a > b:
    for i in range (1, b+1):
        if a * i % b == 0:
            print(a*i)
            break
elif a<b:
    for i in range (1, a+1):
        if b * i % a == 0:
            print(b*i)
            break
else:
    print (a)

