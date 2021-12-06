class Room:
    def __init__(self, intro_1, unique_text, ending_1, ending_2):
        self._room_intro_1 = self.create_scene_string(intro_1)
        self._unique_text = self.create_scene_string(unique_text)
        self._ending_1 = self.create_scene_string(ending_1)
        self._ending_2 = self.create_scene_string(ending_2)

    def get_unique_text(self):
        return self._unique_text
    
    def get_room_intro(self):
        return self._room_intro_1

    def get_ending_1(self):
        return self._ending_1

    def get_ending_2(self):
        return self._ending_2

    def create_scene_string(self, file_name):
        if file_name == " ":
            pass
        else:
            with open(file_name,"rt") as work_file:
                work_string = work_file.read()
            return work_string
