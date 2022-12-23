def show_menu():
    print(f"Выберите действие 1 - показать всех сотрудников"
          " \n 2 - Добавить сотрудника "
          "\n 3 - Удалить сотрудника"
          " \n 4-Выход")
    select = int(input())
    return select


def add_menu():
    print(f"Введите Фамилия Имя Номер телефона через пробел")
    man = input().split()
    return man


def delet_menu():
    print(f"Введите номер записи для удаления")
    delet = int(input())
    return delet


def show_result(msg):
    print(msg)


def show_people(people):
    print("№\tФамилия\tИмя\tНомер телефона")
    for i, p in enumerate(people):
        print(i, *p, sep="\t")
