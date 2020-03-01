from telegram import ReplyKeyboardMarkup

from gamedata import Race, Species


class RegisterKeyboards:

    @staticmethod
    def select_race():
        return ReplyKeyboardMarkup([Race.names], one_time_keyboard=True)

    @staticmethod
    def select_species():
        return ReplyKeyboardMarkup([Species.names], one_time_keyboard=True)