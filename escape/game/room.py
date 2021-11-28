class Room:

    def __init__(self):
        self._adjacent_rooms = []
        self._intro_text = " "
        self._has_visted_room = False
        self._room_text = " "

    def get_adjacent_rooms(self):
        return self._adjacent_rooms

    def get_intro(self):
        return self._intro_text
    
    def get_room_text(self):
        return self._room_text

    def get_visit_status(self):
        return self._has_visted_room

    def set_visit_status(self, status):
        self._has_visted_room = status
    
    def set_adjacent_room(self, room):
        self._adjacent_rooms.append(room)