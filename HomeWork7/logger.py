import builtins
import output


def log_to_file(contact):

    with open('horizontal.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('vertical.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n\n')


def reading_file(param):
    b = output.view()
    if b == 1:
        with open('horizontal.csv', 'r') as file:
            for line in file:
                if param in line:
                    print(line)

    if b == 2:
        list = []
        with open('horizontal.csv', 'r') as file:  
            for line in file:
                if param in line:
                    list = line.split(';')
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n')


def reading_all():
    builtins == output.view()
    if builtins == 1:
        with open('horizontal.csv', 'r') as file:
            for line in file:
                print(line)
    if builtins == 2:
        with open('vertical.csv', 'r') as file:
            for line in file:
                print(line)




def log_to_file(contact):

    with open('horizontal.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('vertical.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n\n')


def reading_file(param):
    b = output.view()
    if b == 1:
        with open('horizontal.txt', 'r') as file:
            for line in file:
                if param in line:
                    print(line)

    if b == 2:
        list = []
        with open('horizontal.txt', 'r') as file:  
            for line in file:
                if param in line:
                    list = line.split(';')
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n')


def reading_all():
    builtins == output.view()
    if builtins == 1:
        with open('horizontal.txt', 'r') as file:
            for line in file:
                print(line)
    if builtins == 2:
        with open('vertical.txt', 'r') as file:
            for line in file:
                print(line)