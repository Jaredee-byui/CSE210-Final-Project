from game.room import Room
from game import room

class Kitchen(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\kitchen_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\kitchen_intro_2.txt")
        self._room_knife = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\kitchen_knife.txt")
        self._adjacent_rooms = ["dining_room", "pantry"]
        self._has_visted_room = False
        self._actions = ["EXIT", "PANTRY"]