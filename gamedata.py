#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Race:
    HUMAN, ELF, ORK = range(3)
    names = ['Человек']
    emoji = ['👨']

class Species:
    WARRIOR, BOWMAN, WIZARD = range(3)
    names = ['Воин', 'Лучник']
    emoji = ['⚔️','🏹']

class MonsterType:
    NORMAL, EXPERT, ELITE, CHAMPION = range(4)


def _read_data(file_name:str) -> list:
    with open(file_name) as file_obj:
        str_data = file_obj.read()
        json_data = json.loads(str_data)
        return json_data


class Gamedata:
    _equipment_armor = None
    _equipment_weapon = None
    _exp_lvl = None
    _item_loot = None
    _location = None
    _monster = None
    stats = None
    primary_loot = None

    @staticmethod
    def load():
        Gamedata._equipment_armor = _read_data('data/equipment_armor.json')
        Gamedata._equipment_weapon = _read_data('data/equipment_weapon.json')
        Gamedata._exp_lvl = _read_data('data/exp_lvl.json')
        Gamedata._item_loot = _read_data('data/item_loot.json')
        Gamedata._location = _read_data('data/location.json')
        Gamedata._monster = _read_data('data/monster.json')
        Gamedata.stats = _read_data('data/stats.json')
        Gamedata.primary_loot = _read_data('data/primary_loot.json')

    @staticmethod
    def validate():
        pass


Gamedata.load()
Gamedata.validate()