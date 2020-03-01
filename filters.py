from telegram.ext import BaseFilter
from telegram import Message, Update
from models.player import Player

class _FilterUniquePlayerName(BaseFilter):
    def filter(self, message:Message):
        name = message.text
        return not Player.is_name_exists(name)

class _FilterIsPlayerExists(BaseFilter):
    def filter(self, message:Message):
        user_id = message.from_user.id
        return Player.is_user_id_exists(user_id)


class CustomFilters():
    unique_player_name = _FilterUniquePlayerName()
    is_player_exists = _FilterIsPlayerExists()