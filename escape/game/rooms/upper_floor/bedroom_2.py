from game.room import Room
from game import room

class Bedroom2(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_2_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_2_intro_2.txt")
        self._room_key = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_2_puzzle_action.txt")
        self._adjacent_rooms = ["hall_1"]
        self._has_visted_room = False
        self._actions = ["EXIT", "CAGE"]