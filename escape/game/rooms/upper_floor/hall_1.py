from game.room import Room
from game import room

class Hall1(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\hall_1_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\hall_1_intro_2.txt")
        self._adjacent_rooms = ["bathrom", "bedroom_1", "bedroom_2", "study"]
        self._has_visted_room = False