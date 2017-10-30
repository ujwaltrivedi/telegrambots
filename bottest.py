from telegram.ext import Updater, CommandHandler
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import telegram

inlinekeyboard = [[InlineKeyboardButton("Show Recall", callback_data=8342),
                    InlineKeyboardButton("Hide Recall", callback_data=0)]]

reply_markup = InlineKeyboardMarkup(inlinekeyboard)


chat_id=-260850066
access_token = 'you-access-token=here'

bot = Bot(access_token)
bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
bot.send_message(chat_id=chat_id, text="Custom Keyboard Test, Reply.", reply_markup=reply_markup)
#bot.send_photo(chat_id=chat_id, photo="")
