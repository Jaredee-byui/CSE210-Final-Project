class Room:
    def __init__(self, visit_status, intro_1, unique_text, ending_1, ending_2, adjacent_rooms, actions):
        self._has_visted_room = visit_status
        self._room_intro_1 = self.create_scene_string(intro_1)
        self._unique_text = self.create_scene_string(unique_text)
        self._adjacent_rooms = adjacent_rooms
        self._actions = actions
        self._ending_1 = self.create_scene_string(ending_1)
        self._ending_2 = self.create_scene_string(ending_2)

    def get_adjacent_rooms(self):
        return self._adjacent_rooms

    def get_unqiue_text(self):
        return self._unique_text
    
    def get_room_intro(self):
        return self._room_intro_1

    def get_ending_1(self):
        return self._ending_1

    def get_ending_2(self):
        return self._ending_2

    def get_visit_status(self):
        return self._has_visted_room

    def set_visit_status(self, status):
        self._has_visted_room = status

    def create_scene_string(self, file_name):
        with open(file_name,"rt") as work_file:
            work_string = work_file.read()
        return work_string

    def get_actions(self):
        return self._actions