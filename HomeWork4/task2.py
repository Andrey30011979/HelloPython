# 2.	Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
while i <= N:
    if N % i == 0:
        lst.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {N} приведены в списке: {lst}")