# 5.Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст, причём число строк заранее неизвестно.
# Ваша задача – пронумеровать слова в нём, начиная с нуля, а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. (В решении задачи поможет функция enumerate())
# Входные данные	               Выходные данные
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Сунул в реку руку Грека.
# Рак за руку Греку цап.
# 	                                4 - Видит
#                                   1 - Грека
#                                   17 - Греку
#                                   0 - Ехал
#                                   14 - Рак
#                                   9 - Сунул
text = ["Ехал", "Грека", "через", "реку", "Видит", "Грека", "в", "реке", "рак", "Сунул", "в",
        "реку", "руку", "Грека", "Рак", "за", "руку", "Греку", "цап"]
text = enumerate(text)
text = list(filter(lambda x:x[1][0].isupper(),text))
text.sort(key = lambda x:x[1])
sp = []
for x,y in text:
    if y not in sp:
        print(x,"-",y)
    sp.append(y)
# print(list(text))