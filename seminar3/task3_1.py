# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	      1

sp = [int(I) for I in input().split()]
for element in sp:
    if sp.count(element) == 1:
        print(element)