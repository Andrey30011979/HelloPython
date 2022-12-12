# 5.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные	Выходные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye	          Bye

slovar = {}
for i in range (3):
    key, value = input().split()
    slovar[key] = value
print(slovar) 
a = input('введите слово')
for key, value in slovar.items():
    if a == key:
        print(value)
    elif a == value:
        print(key)