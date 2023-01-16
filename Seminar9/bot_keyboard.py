import random
import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
candies = 0

reply_keyboard = [['/rules', '/game'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN ="5945103866:AAHMIjz3zQtEpMOVs2iYhXZxmpivubYQDOY"


def start(update, context):
    update.message.reply_text(
        f"Привет давай поиграем.\n"
        "/game-начать игру.\n"
        "/rules-правила игры.\n"
        "/exit-выйти\n",
        reply_markup=markup
    )

def game(update, context):
    update.message.reply_text(
        "Введите количество конфет для игры",
        reply_markup=ReplyKeyboardRemove()
    )
    return 1

def rules(update, context):
    update.message.reply_text(
        """Игроки ходят по очереди,каждый игрок может взять не больше 28 конфет,
        выигрывает тот кто взял последнии конфеты. """)


def exit(update, context):
    update.message.reply_text(
        "Досвидание.",reply_markup=ReplyKeyboardRemove())


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END 


def init_game(update, context):
    global candies
    try:
        candies = int(update.message.text)
        update.message.reply_text(f"На кану {candies} конфет.")
        update.message.reply_text("Ваш ход. Сколько хотите взять конфет.")
        return 2
    except:
        update.message.reply_text("Введите число")


def level_game(update, context):
    global candies
    candies1 = int(update.message.text)
    if candies1 > 28 or candies1 < 1:
        update.message.reply_text("Введите коректное число")
        return 2
    candies = candies - candies1
    if candies >= 29:
        update.message.reply_text(f"Накану осталось{candies} конфет. Мой ход")
        candies2 = random.randint(1, 28)
        update.message.reply_text(f"Я беру{candies2} конфет")
        candies = candies - candies2
        if candies >= 29:
            update.message.reply_text(f"На кану {candies} конфет.")
            update.message.reply_text("Ваш ход. Сколько хотите взять конфет.")
            return 2 
        else:
            update.message.reply_text("Ты победил!",reply_markup=markup) 
    else:
        update.message.reply_text("Победил Я!",reply_markup=markup)
    return ConversationHandler.END 




    
game_handler = ConversationHandler(
entry_points=[CommandHandler('game', game)],
    states={   
        1: [MessageHandler(Filters.text & ~Filters.command, init_game)],
        2: [MessageHandler(Filters.text & ~Filters.command, level_game)],   
        },
       fallbacks=[CommandHandler('stop', stop)]
       
    )




def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(game_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))
 

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()