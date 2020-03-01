from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

from filters import CustomFilters
from handlers.utils import not_valid_data
from keyboards import RegisterKeyboards
from message import RegisterMessage
from models.player import Player
from regex import RegisterRegex


class StateRegister:
    ENTER_NAME, SELECT_RACE, SELECT_SPECIES = range(3)


def start_new_player(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.hello_new_player(),
                             reply_markup=None
                             )
    return StateRegister.ENTER_NAME


def enter_valid_name(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    name: str = update.message.text
    context.user_data['name'] = name
    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.select_race(),
                             reply_markup=RegisterKeyboards.select_race()
                             )
    return StateRegister.SELECT_RACE


def enter_invalid_name(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.invalid_name(),
                             reply_markup=None
                             )


def enter_not_unique_name(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.not_unique_name(),
                             reply_markup=None
                             )


def select_race(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    race = update.message.text
    context.user_data['race'] = race
    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.select_species(),
                             reply_markup=RegisterKeyboards.select_species()
                             )
    return StateRegister.SELECT_SPECIES


def select_species(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    species: str = update.message.text
    context.user_data['species'] = species

    Player.register_player(update.effective_user.id, context.user_data['name'], context.user_data['race'],
                           context.user_data['species'])

    context.bot.send_message(chat_id=chat_id,
                             text=RegisterMessage.finish_register()
                             )
    return ConversationHandler.END


register_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_new_player, filters=~CustomFilters.is_player_exists)],
    states={
        StateRegister.ENTER_NAME: [
            MessageHandler(Filters.regex(RegisterRegex.valid_name) & CustomFilters.unique_player_name,
                           enter_valid_name),
            MessageHandler(~CustomFilters.unique_player_name, enter_not_unique_name),
            MessageHandler(~Filters.regex(RegisterRegex.valid_name), enter_invalid_name)
        ],
        StateRegister.SELECT_RACE: [
            MessageHandler(Filters.regex(RegisterRegex.valid_race), select_race),
            MessageHandler(Filters.all, not_valid_data)
        ],
        StateRegister.SELECT_SPECIES: [MessageHandler(Filters.regex(RegisterRegex.valid_species), select_species)]
    },
    fallbacks=[]

)
