# 4.	Вводится список целых чисел в одну строчку через пробел.
#  Необходимо оставить в нем только двузначные числа.
#  Реализовать программу с использованием функции filter.
#  Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#  пример  - 8 11 0 -23 140 1 => 11 -23

sp = [ - 8, 11, 0, -23, 140, 1]
sp = filter(lambda x: 10 <= abs(x) < 100, sp)
print(list(sp))