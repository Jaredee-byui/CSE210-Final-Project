from game.room import Room
from game import room

class FoyerCloset(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_closet_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_closet_intro_2.txt")
        self._room_umbrella = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_closet_umbrella.txt")
        self._adjacent_rooms = ["foyer"]
        self._has_visted_room = False
        self._actions = ["EXIT", "UMBRELLA"]