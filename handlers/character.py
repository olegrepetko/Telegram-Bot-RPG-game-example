from telegram import Update
from telegram.ext import CallbackContext

from models.player import Player
from message import CharacterMessage


def character_info(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    print(update.effective_user.id)
    player = Player.get_player_by_user_id(update.effective_user.id)
    print(player)
    context.bot.send_message(chat_id=chat_id,
                             text=CharacterMessage.info(player)
                             )
