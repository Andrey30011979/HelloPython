# 3.	Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел,
#  делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# sp = range(10, 100)
# sp = filter(lambda x: x % 9 == 0, sp)
# sp = map(lambda x: x ** 2, sp)
# print(list(sp))


sp = range(10, 100)
sp = filter(lambda x: x % 9 == 0, sp)
sp = map(lambda x: x ** 2, sp)
print(sum(sp))

# sp = [i**2 for i in range(10,100) if i % 9 == 0]
# print(sum(sp))