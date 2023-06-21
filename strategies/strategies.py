from telebot import types
from errors.setup_logger import logger
from time import sleep


def rsi_notification(stock, bot, chats):
    try:
        bot.keyboard1 = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text=f"{stock.ticker}",
                                             url=f"https://www.tinkoff.ru/invest/stocks/{stock.ticker}")
        bot.keyboard1.add(url_btn)
        
        old_rsi = stock.old_levels.get("RSI")
        current_rsi = stock.levels.get("RSI")
        # attention to sell
        if old_rsi and old_rsi < 80 < current_rsi:
            attention = "\U000026A0"
            print(f'RSI is overbought ({current_rsi}), be careful!')
            for chat in chats:
                bot.send_message(chat,
                             f"{attention}${stock.ticker} <b>RSI</b> is overbought ({round(current_rsi, 2)}), "
                             f"be careful!{attention}",
                             parse_mode="HTML", reply_markup=bot.keyboard1)
                sleep(4)
        # sell
        if old_rsi and old_rsi > 80 > current_rsi:
            attention = "\U0000203C"
            print(f'RSI cross downward 80 ({current_rsi}), time to sell!')
            for chat in chats:
                bot.send_message(chat,
                             f"{attention}${stock.ticker} <b>RSI</b> cross downward 80 ({round(current_rsi, 2)}), time to sell!\U0001F534{attention}",
                             parse_mode="HTML", reply_markup=bot.keyboard1)
                sleep(4)
        # attention to buy
        if old_rsi and old_rsi > 30 > current_rsi:
            attention = "\U000026A0"
            print(f'RSI is oversold ({current_rsi}), be careful!')
            for chat in chats:
                bot.send_message(bot.chat_id,
                             f"{attention}${stock.ticker} <b>RSI</b> is oversold ({round(current_rsi, 2)}), be "
                             f"careful!{attention}",
                             parse_mode="HTML", reply_markup=bot.keyboard1)
                sleep(4)
        # buy
        if old_rsi and old_rsi < 30 < current_rsi:
            attention = "\U0000203C"
            print(f'RSI cross upward 20 ({current_rsi}), time to buy!')
            for chat in chats:
                bot.send_message(chat,
                             f"{attention}${stock.ticker} <b>RSI</b> cross upward 20 ({round(current_rsi, 2)}), "
                             f"time to buy!\U0001F7E2{attention}",
                             parse_mode="HTML", reply_markup=bot.keyboard1)
                sleep(4)
        stock.old_levels["RSI"] = stock.levels.get("RSI")
    except Exception as e:
        logger.exception(f"Exception in rsi method: \n{e}\n")
    