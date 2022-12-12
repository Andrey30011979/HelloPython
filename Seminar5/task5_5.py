# 5.	Дан список, вывести отдельно буквы и цифры.
# a = ( '1', 'a', 'b', '2', '3' ,'c') 
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

spa =  ['1', 'a', 'b', '2', '3' ,'c']
spb = filter(lambda x: x.isalpha(), spa)
spc = filter(lambda x: x.isdigit(), spa)
print(list(spb))
print(list(spc))