# import logging

# # если хотим, чтобы логи выводились в консоль
# logging.basicConfig(level=logging.INFO)

# # если хотим, чтобы логи записывались в файл
# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.INFO,
#                     encoding="utf-8")

# def main():
#     …
#     logging.info("Данные от пользователя получены")

#     …
#     logging.warning("Ошибка обработки данных")

import logging
import view
import model
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding="utf-8")


def main():
    select = view.showmenu()
    if select == "1":
        logging.info('Выбран режим калькулятор')
        x = view.get_ix()
        res = model.calc(x)
        view.showres(res)
        logging.info('Напечатан результат')
    if select == "2":
        logging.info('Выбран режим конвертор')
        m = view.get_m()
        res = model.convert(m)
        view.showresm(res)
        logging.info('Напечатан результат')



