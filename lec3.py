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

sum = lambda x, y: x+y                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          # f = lambda q, w: q+w #f = sum

def mylt(x, y):
    return x*y

def calc(op, a, b):
     print(op(a, b)) # return op(a, b)
   
calc(mylt, 4, 5)
calc(sum, 5, 5) # calc(f, 4, 5)
