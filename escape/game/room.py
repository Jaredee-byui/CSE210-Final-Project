class Room:

    def __init__(self):
        self._adjacent_rooms = []
        self._room_intro_1 = " "
        self._has_visted_room = False
        self._room_intro_2 = " "

    def get_adjacent_rooms(self):
        return self._adjacent_rooms

    def get_intro(self):
        return self._intro_text
    
    def get_room_intro_1(self):
        return self._room_intro_1

    def get_room_intro_2(self):
        return self._room_intro_2

    def get_visit_status(self):
        return self._has_visted_room

    def set_visit_status(self, status):
        self._has_visted_room = status
    
    def set_adjacent_room(self, room):
        self._adjacent_rooms.append(room)

    def create_scene_string(self, file_name):
        with open(file_name,"rt") as work_file:
            work_string = work_file.read()
        return work_string