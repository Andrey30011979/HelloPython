# Анонимные, lambda функции

# def f(x):
#     x ** 2

# g = f
# print(f(1))  # None
# print(g(1))  # None

# def f(x):
#     return x**2
# print(f(2))

# print(type(f)) # <class 'function'>

# def f(x):
#     return x**2

# g = f

# print(type(f)) # <class 'function'>
# print(type(g)) # <class 'function'>

# print(f(4))  # 16
# print(g(4))  # 16

# def calc1(x):
#     return x+10
# print(calc1(10))
# def calc2(x):
#     return x*10
# print(calc2(10))


# def f(x):
#     return x**2

# g = f

# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y

# f = lambda q, w: q+w #f = sum
# def sum(x, y): return x+y

# sum = lambda x, y: x+y + 1

# def mylt(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))  # return op(a, b)


# calc(lambda x, y: x+y , 4, 5)
# calc(sum, 5, 5)  # calc(f, 4, 5)


# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#         list.append(i);

# print   (list)

# list =[i for i in range(1,21)if i % 2 == 0]
# print(list)
# list =[(i, i) for i in range(1,21)if i % 2 == 0]
# print(list)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

# def f(x):
#     return x**3

# list =[f(i) for i in range(1,21)if i % 2 == 0]
# print(list) # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

# def f(x):
#     return x**3

# list =[(i, f(i)) for i in range(1,21)if i % 2 == 0]
# print(list)  #[(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]

# def select(f, col):
#  return [f(x) for x in col]
# def where(f, col):
#  return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# # data = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)

# print(res) # [(2, 4), (8, 64), (38, 1444)]

# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)

# data = list(map(int,'1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)

# data = [x for x in range(10)]
# res =list(filter(lambda x: not x % 2, data))
# print(res)

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

