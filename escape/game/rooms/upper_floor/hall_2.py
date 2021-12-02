from game.room import Room
from game import room

class Hall2(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\hall_2_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\hall_2_intro_2.txt")
        self._adjacent_rooms = ["music_room", "master_bed"]
        self._has_visted_room = False
        self._actions = ["MUSIC ROOM", "MASTER BEDROOM", "EXIT"]