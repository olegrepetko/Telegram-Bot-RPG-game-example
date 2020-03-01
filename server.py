#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher

from models.player import Player
from handlers.register import register_handler
from handlers.character import character_info

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')

def delete_me(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    Player.delete_player(update.effective_user.id)
    context.bot.send_message(chat_id=chat_id, text="Deleted.")


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("API_KEY", use_context=True)

    dp: Dispatcher = updater.dispatcher

    dp.add_handler(register_handler)

    dp.add_handler(CommandHandler('delete_me', delete_me))
    dp.add_handler(CommandHandler('info', character_info))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
