from telegram import Update, Message
from telegram.ext import CallbackContext

def not_valid_data(update: Update, context: CallbackContext):
    msg: Message = update.message
    msg.delete()