# 6.	Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

str_1 = "мама мммммыла раму"
str_2 = "мм"

i = 0
count = 0
while i < len(str_1):
    res = True
    for j in range(len(str_2)):
        if str_1[i] != str_2[j]:
            res = False 
        i += 1    
    if res == True:
        count += 1 
print(count)
