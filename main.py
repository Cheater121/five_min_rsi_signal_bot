import telebot

from telebot import custom_filters
from time import sleep

from stocks.stock_info import stocks_list
from errors.setup_logger import logger
from strategies.strategies import rsi_notification
from utils.timers import time_checker
from config_data.config import load_config

config = load_config()

TG_5MIN_TOKEN = config.tg_bot.token
chats = config.tg_bot.chats

bot = telebot.TeleBot(TG_5MIN_TOKEN)
bot.update_switcher = True


@bot.message_handler(chat_id=chats, commands=['start'])
def start_handler(message):
    try:
        bot.send_message(message.chat.id,
                         f"Hello! Prepare for spam. To stop it use '/stop' command. And '/help' for all commands. Your chat id is {message.chat.id}")
        bot.chat_id = message.chat.id
        bot.update_switcher = True
        while bot.update_switcher:
            if time_checker():
                for stock in stocks_list:
                    sleep(1)  # Delay for Tinkoff API
                    stock.get_new_prices()
                    rsi_notification(stock, bot, chats)
            sleep(1)
    except Exception as e:
        logger.exception(f"Exception in start handler: \n{e}\n")


@bot.message_handler(chat_id=chats, commands=['stop'])
def stop_handler(message):
    try:
        bot.send_message(message.chat.id, "Bye bye! To start use '/start'.")
        bot.update_switcher = False
    except Exception as e:
        logger.exception(f"Exception in stop handler: \n{e}\n")


@bot.message_handler(chat_id=chats, commands=['status'])
def status_checker(message):
    try:
        if bot.update_switcher is True:
            on_off = "on"
        else:
            on_off = "off"
        bot.reply_to(message, f"I'm fine, thanks! Update switcher is {on_off}")
    except Exception as e:
        logger.exception(f"Exception in status checker:\n{e}\n")


@bot.message_handler(chat_id=chats, commands=['stocks'])
def stock_handler(message):
    try:
        bot.send_message(message.chat.id,
                         "OZON, SBER, SGZH, POLY, VKCO, TATN, NVTK, SPBE, NLMK, PIKK, FIVE, AFKS, YNDX, ROSN, ALRS, "
                         "GMKN, AFLT, GAZP, LKOH, MOEX")
    except Exception as e:
        logger.exception(f"Exception in stock handler: \n{e}\n")


@bot.message_handler(chat_id=chats, commands=['help'])
def help_handler(message):
    try:
        bot.send_message(message.chat.id,
                         "I have commands: '/start' (for admins), '/stop' (for admins), '/status' (for admins), "
                         "'/stocks' (for all members) - send tracked stocks list.")
    except Exception as e:
        logger.exception(f"Exception in help handler: \n{e}\n")


if __name__ == "__main__":
    print("start")
    bot.add_custom_filter(custom_filters.ChatFilter())
    bot.polling()
    print("finished")
    