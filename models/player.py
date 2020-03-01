from db import db
from gamedata import Gamedata, Race, Species, MonsterType

class Player:

    @staticmethod
    def register_player(user_id: int, name: str, race: str, species: str):
        race_id = Race.names.index(race)
        species_id = Species.names.index(species)

        stats: dict = Gamedata.stats['primary']
        inventory: dict = Gamedata.primary_loot['race'][race_id] + Gamedata.primary_loot['species'][species_id]

        player = {
            "user_id": user_id,
            "name": name,
            "race": race_id,
            "exp": 0,
            "lvl": 1,
            "silver": 0,
            "energy": 100,
            "species": species_id,
            "stats": stats,
            "inventory_size": 100,
            "inventory": inventory
        }

        db.players.insert_one(player)

    @staticmethod
    def is_user_id_exists(user_id: int) -> bool:
        player = db.players.find_one({"user_id": user_id})
        return player is not None

    @staticmethod
    def is_name_exists(name: str) -> bool:
        player = db.players.find_one({"name": name})
        return player is not None

    @staticmethod
    def get_player_by_user_id(user_id):
        player = db.players.find_one({"user_id": user_id})
        return player

    @staticmethod
    def delete_player(user_id):
        db.players.delete_one({"user_id": user_id})
