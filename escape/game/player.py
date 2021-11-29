
class Player:
    def __init__(self):
        self._inventory = {
            "book_1": False,
            "book_2": False,
            "knife": False,
            "umbrella": False,
            "magnifying glass": False,
            "key_mb": False,
            "key_cellar": False
        }
        self._current_room = None
        self._previous_room = None

    def get_inventory(self):
        return self._inventory

    def get_current_location(self):
        return self._current_room

    def get_item_value(self, key):
        return self._inventory[key]

    def add_item_inventory(self, key, value):
        self._inventory[key] = value

    def get_previous_location(self):
        return self._previous_room
    
    def set_current_room(self, room):
        self._previous_room = self._current_room
        self._current_room = room
        
