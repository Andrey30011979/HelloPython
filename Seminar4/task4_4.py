# 4.	В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Входные данные	      Выходные данные
# one two one tho three	   0 0 1 0 0

stroka = "one two one tho three".split()
slovar = {}
for i in stroka:
    slovar[i] = slovar.get(i, -1) + 1
    print(slovar[i],end=" ")
print(slovar)