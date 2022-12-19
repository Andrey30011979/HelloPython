def showmenu():
    print("Выберете действия:\n1- калькулятор\n2-конвертер")
    select = input()
    return select

def get_ix():
    x = input('Введите выражение')
    return x

def get_m():
    m = int(input('Введите массу в кг ')) 
    return m  

def showres(res):
    print(f"Результат: {res}")

def showresm(res):
    print(f"Масса в граммах = {res}")

    
