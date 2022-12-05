# print('Hello world')
# Переменные
# Типы данных справедливы
# int, float, boolean, str
# list и др.
# Python – язык с динамической типизацией
# value = 2809
# name = 'Sergey'

# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value  = 12334
# print(type(value))

# a = 123
# b = 1.23
# s = 'Hello world'
# # s = "Hello 'world"
# # s = 'Hello "world'    
# # s = 'Hello \nworld'   #перенос строки \n
# # print(s) #вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f)
# f = False
# print(f)

# list = []
# list = ['1', '2', '3', 'hello world']
# print(list)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)
 
# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)

# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+', b, '=', a+b)

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+', b, '=', a+b)

# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +, -,*, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 123
# b = -321
# c = a + b
# print(c)

# a = 2
# b = 8
# c = a - b
# print(c)

# a = 2
# b = 8
# c = a * b
# print(c)

# a = 2
# b = 8
# c = a / b
# print(c)

# a = 12
# b = 5
# c = a // b # деление в целых числах
# print(c)

# a = 12
# b = 8
# c = a % b # остаток от деления
# print(c)

# a = 2
# b = 800
# c = a ** b # возведение в степень
# print(c)

# a = 1.3123
# b = 3
# c = round(a * b, 5)
# print(c)

# Операции присваивания
# Сокращённые операции и операции присваивания
# Демонстрация
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# a = 3
# a += 5 # a = a + 5
# print(a)

# a = 3
# a *= 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 2 # True
# print(a)

# a = 1 > 4 and 5 > 2 # False
# print(a)

# a = 'gwe'
# b = 'gwe'
# print(a == b) # получим True

# a = [1,2]
# b = [1,2]
# print(a == b)  #сравнение списков

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = 1 < 2 or 4 > 6 #  если одно высказывание истина то получим True
# print(f)

# f =[1,2,3,4]
# print(f)
# print(2 in f) # True
# f =[1,2,3,4]
# print(f)
# print(not 2 in f) # False

# f =[1,2,3,4]
# is_odd = f[0] % 2 == 0
# print(is_odd)
# f =[1,2,3,4]
# is_odd = not f[0] % 2 
# print(is_odd)

# Управляющие конструкции: if, if-else
# if condition:
 # operator 1
 # operator 2
 # ...
 # operator n
# else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Управляющие конструкции: if, if-else
# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator 

# username = input('Введите имя:')
# if username == 'Лена':
#     print('Ура ,это же Лена')
# elif username == 'Елена':
#     print('Я так ждал вас Елена')
# elif username == 'Андрей':
#     print('Андрей - топ)')
# else:
#     print('Привет', username)

# Управляющие конструкции: while
# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # . . .
#  # operator n + m

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in enumeration:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i**2)

# r = range(10) # получаем значения от 0 до 10
# for i in r:
#     print(i)

# for i in range(1, 5):#  диапазон
#     print(i)    

# for i in range(1, 10, 2): # увеленчение на 2
#     print(i)      

# for i in 'qwe - rty':
#     print(i)  

# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# Списки: введение
# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый
# многократно
# def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

# def f(x):
#  return x**2
# def f(x):
#  if x == 1:
#      return 'Целое'
#  elif x == 2.3:
#     return 23
#  else:
#     return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # Non 