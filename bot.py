from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

access_token = 'you-access-token=here'

inlinekeyboard = [[InlineKeyboardButton("Show Recall", callback_data='1'),
					InlineKeyboardButton("Hide Recall", callback_data='2')]]

reply_markup = InlineKeyboardMarkup(inlinekeyboard)

def start(bot, update):
	update.message.reply_text('Hello World!')


def hello(bot, update):
	if update.message.from_user.username == "ujwalt":
		update.message.reply_text('Hello {}'.format(update.message.from_user.first_name), reply_markup=reply_markup)


def button(bot, update):
	query = update.callback_query
	bot.edit_message_text(text="{} -- Selected option: {}".format(query.message.text, query.data),
							chat_id=query.message.chat_id,
							message_id=query.message.message_id)


updater = Updater(access_token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
