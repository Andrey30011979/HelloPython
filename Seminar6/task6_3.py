# 3.	Дан список чисел. Вывести из него только простые числа.
# Ввод	    Вывод
# 15 2 3 31	2 3 31
def prost(i):
    for j in range(2,i//2+1):
        if i%j == 0:
            return False
    return True


sp = [15, 2, 3, 31]
# res = list(filter(prost,sp))
# print(res)

res = []
for i in sp:
    if prost(i):
        res.append(i)
print(res)