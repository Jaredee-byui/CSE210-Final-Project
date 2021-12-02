from game.room import Room
from game import room

class Study(Room):
    def __init__(self):
        self._room_intro_1 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\study_intro_1.txt")
        self._room_intro_2 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\study_intro_2.txt")
        self._room_book_1 = room.create_scene_string(r"escape\game\rooms\upper_floor\upper_floor_text\search_desk.txt")
        self._adjacent_rooms = ["hall_1"]
        self._has_visted_room = False
        self._actions = ["EXIT", "DESK"]