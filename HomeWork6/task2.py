# 2.Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные                                           Выходные данные
# ОРРОРОРООРРРО                                                 3
# ООООООРРРОРОРРРРРРР                                           7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР      31

s = input()
count = 0
max = 0
for i in range(len(s)):
    if s[i] == 'Р':
        count += 1
    if count > max:
        max = count
    if i + 1 < len(s):
        if s[i + 1] == 'О':
            count = 0
print(max)
