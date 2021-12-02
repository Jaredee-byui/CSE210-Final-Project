from game.room import Room
from game import room

class StairCase(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\staircase_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\staircase_intro_2.txt")
        self._adjacent_rooms = ["foyer", "landing"]
        self._has_visted_room = False
        self._actions = ["EXIT", "LANDING"]