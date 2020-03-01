from gamedata import Race


class RegisterMessage:

    @staticmethod
    def hello_new_player():
        return """Добро пожаловать в нашу фэнтезийную игру!
Исследуйте огромную Карту мира, чтобы обрести знания мудрых предков и обнаружить новые технологии. Торгуйтесь или сражайтесь за мощные Реликвии, увеличивающие производство.

Герой как тебя зовут?
    """

    @staticmethod
    def invalid_name():
        return """Имя может быть только с символов!"""

    @staticmethod
    def not_unique_name():
        return """Герой с таким именем уже существует!"""

    @staticmethod
    def select_race():
        return f"""Отлично!
Выбери свою расу:"""

    @staticmethod
    def select_species():
        return """Отлично!
Выбери свой класс: """

    @staticmethod
    def finish_register():
        return """Отлично!
/delete_me - удалить акк
/info - инфо"""

class CharacterMessage:

    @staticmethod
    def info(player):
        return f"""
Раса: {Race.names[player['race']]} {Race.emoji[player['race']]}
Класс: 
        """
