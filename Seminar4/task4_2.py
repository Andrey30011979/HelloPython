# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

# f = "5x^2 + 3x + -7 = 0"
# f = f[:-3]
# print(f)
# f = f.split("+")
# print(f)
# list = []
# for i in f:
#     list.append(int(i.split("x")[0]))
# print(list)
# a, b, c = list
# d = b**2 -4 * a * c
# print(d)
# if d>0:
#     x1 = round((-b - d**0.5)/(2*a), 2)
#     x2 = round((-b + d**0.5)/(2*a), 2)
#     print (x1, x2)
# elif d == 0:
#     x1 = (-b)/(2*a)
#     print(x1)
# else:
#     print('Корней нет')

import math

f = "5x^2 + 3x + -7 = 0"
f = f[:-3]
print(f)
f = f.split("+")
print(f)
list = []
for i in f:
    list.append(int(i.split("x")[0]))
print(list)
a, b, c = list
d = b**2 -4 * a * c
print(d)
if d>0:
    x1 = round((-b - math.sqrt(d))/(2*a), 2)
    x2 = round((-b + math.sqrt(d))/(2*a), 2)
    print (x1, x2)
elif d == 0:
    x1 = (-b)/(2*a)
    print(x1)
else:
    print('Корней нет')