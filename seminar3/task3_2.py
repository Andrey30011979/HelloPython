# 2.	Дан список чисел. Выведите все элементы списка, 
# которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	           5 4
sp = [int(I) for I in input().split()]
for i in range(len(sp)- 1):
    if sp[i] < sp[i + 1]:
        print(sp[i +1], end = " ")
