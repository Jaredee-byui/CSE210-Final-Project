
class Player:
    def __init__(self):
        self._inventory = {}
        self._current_room = " "

    def get_inventory(self):
        return self._inventory

    def get_location(self):
        return self._current_room

    def add_item_inventory(self, key, value):
        self._inventory[key] = value

