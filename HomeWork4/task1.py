# 1.	Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Введите степень округления в формате 0.001:')
d = d[2:len(d)]
print(round(math.pi,len(d)))
 

