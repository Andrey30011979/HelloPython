# Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится лук. Переписывайте без него.

# Формат ввода
# На первой строке вводится натуральное число N — количество пунктов рецепта.
# Далее следуют N строк — пункты рецепта.

# Формат вывода
# Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием лука (то есть таких, в которых нет подстроки "лук" в нижнем регистре).

# Пример
# Ввод	                              Вывод
# 5
# лук 1 головка
# картофелин штук 6
# картошку почистить
# лук порезать кольцами
# зажарить всё
# #                                картофелин штук 6, картошку почистить, зажарить всё
sp = []
n = int(input())
for i in range(n):
    s = input()
    sp.append(s)


sp = filter(lambda x:"лук" not in x,sp)
print(', '.join(sp))