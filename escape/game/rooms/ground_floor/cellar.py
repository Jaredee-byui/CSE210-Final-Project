from game.room import Room
from game import room

class cellar(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\cellar_intro_1.txt")
        self._room_good_end = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\cellar_good_end.txt")
        self._room_bad_end = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\cellar_bad_end.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\cellar_joke_end.txt")
        self._adjacent_rooms = ["foyer"]
        self._has_visted_room = False
        self._actions = ["FORGIVE"]