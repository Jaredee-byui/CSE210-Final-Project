from game.room import Room
from game import room

class Foyer(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_intro_2.txt")
        self._room_door = room.create_scene_string(r"escape\game\rooms\ground_floor\ground_floor_text\foyer_door.txt")
        self._adjacent_rooms = ["cellar", "den", "dining_room", "foyer_closet", "staircase"]
        self._has_visted_room = False
        self._actions = ["DOOR", "CELLAR", "DEN", "DINING ROOM", "FOYER CLOSET", "STAIRCASE"]
    
