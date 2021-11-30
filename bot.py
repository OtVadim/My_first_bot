import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def talk_to_me(update, context):      #   функция, выполняющая роль эхо
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Ну привет..')


def wordcount(update, context):    #  функция, которая считает количество слов
    print('Вызван /wordcount')
    update.message.reply_text('посчитаем слова...')
    user_text = update.message.text
    create_sp = user_text.split() 
    print(len(create_sp)-1)
    update.message.reply_text(len(create_sp)-1)


def planet(update, context):      #  функция с модулем ephem
    print('Вызван /planet')
    user_text = update.message.text
    spl_user_text = user_text.split()
    if spl_user_text[1] == 'Mars':
        pl = ephem.Mars('2021/11/30')
    constellation = ephem.constellation(pl)
    print(constellation)
    update.message.reply_text(constellation)


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
    logging.info("Bot Started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()