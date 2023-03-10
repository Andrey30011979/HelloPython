# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# with open('file.txt', 'a') as data:
#  data.write('line 1111\n')
#  data.write('line 2222\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# patch = 'file.txt'
# data = open(patch, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()

# def f(x):
#  return x**2
# def f(x):
#  if x == 1:
#   return 'Целое'
#  elif x == 2.3:
#   return 23
#  else:
#   return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type)

# def new_string(symbol, count):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required

# def new_string(symbol, count = 3):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# def concatenatio(*params):
#  res: str = ""
#  for item in params:
#      res += item
#  return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# def fib(n):
#  if n in [1, 2]:
#   return 1
#  else:
#   return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# Кортежи
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# a = (3, 4)
# print(a) # (3, 4)

# a = (3, 4)
# print(a[-1]) # 4

# a = (3, 2, 3, 5, 4)
# print(a[-2]) # 5

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range

# t = tuple(['red', 'green', 'blue'])
# print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range

# t = tuple(['red', 'green', 'blue'])
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# # item assignment

# a = (3, 4, 5)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# Словари
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }

# for k in dictionary.values(): # ↑ ← ↓ →
#   print(k)                  

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }

# for v in dictionary: 
#     print(dictionary[v])  

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# print(c)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# print(i)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# dl = a.difference(b) # dl = {1, 3}
# print(dl)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# dr = b.difference(a) # dr = {13, 21}
# print(dr)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# q = a \
#   .union(b) \
#   .difference(a.intersection(b))
# print(q)
# # {1, 21, 3, 13}

# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# list1 =[1,2,3,4,5]
# list2 = list1
# list1[0] = 123
# list1[1]=333
# for e in list1:
#     print(e)

# print()
# for e in list2:
#     print(e)    

# list1 =[1,2,3,4,5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# list1 =[1,2,3,4,5]
# print(list1.pop(2))
# print(list1)

# list1 =[1,2,3,4,5]
# print(list1.insert(2, 11))
# print(list1)

# list1 =[1,2,3,4,5]
# print(list1.append(311))
# print(list1)