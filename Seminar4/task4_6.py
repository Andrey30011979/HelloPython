# 6.	Дан текст: в первой строке задано число строк, далее идут сами строки. 
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов 
# несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные	                     Выходные данные
# 1                                       banana
# apple orange banana banana orange	        

slovar = {}
stroka = "apple orange banana banana orange".split(" ")
for i in stroka:
    slovar[i] = slovar.get(i, 0) + 1
print(slovar)
maxi = max(slovar.values())
mini = "z"
for key, value in slovar.items():
    if value == maxi:
        if key < mini:
            mini = key
print(mini)
