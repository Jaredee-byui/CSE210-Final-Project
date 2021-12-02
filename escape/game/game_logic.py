from game.room import Room
from game.player import Player

class GameLogic:
    def __init__(self, rooms, player, user_input):
        self._rooms = rooms
        self._player = player
        self._user_input = user_input
        self.handle_logic()

    def handle_logic(self):
        if self._player.get_current_location() == self._rooms[0]:
            self.handle_cellar()
        elif self._player.get_current_location() == self._rooms[1]:
            self.handle_den()
        elif self._player.get_current_location() == self._rooms[2]:
            self.handle_dining_room()
        elif self._player.get_current_location() == self._rooms[3]:
            self.handle_foyer_closet()
        elif self._player.get_current_location() == self._rooms[4]:
            self.handle_foyer()
        elif self._player.get_current_location() == self._rooms[5]:
            self.handle_kitchen()
        elif self._player.get_current_location() == self._rooms[6]:
            self.handle_pantry()
        elif self._player.get_current_location() == self._rooms[7]:
            self.handle_staircase()
        elif self._player.get_current_location() == self._rooms[8]:
            self.handle_bathroom()
        elif self._player.get_current_location() == self._rooms[9]:
            self.handle_bedroom_1()
        elif self._player.get_current_location() == self._rooms[10]:
            self.handle_bedroom_2()
        elif self._player.get_current_location() == self._rooms[11]:
            self.handle_hall_1()
        elif self._player.get_current_location() == self._rooms[12]:
            self.handle_hall_2()
        elif self._player.get_current_location() == self._rooms[13]:
            self.handle_landing()
        elif self._player.get_current_location() == self._rooms[14]:
            self.handle_master_bath()
        elif self._player.get_current_location() == self._rooms[15]:
            self.handle_master_bed()
        elif self._player.get_current_location() == self._rooms[16]:
            self.handle_music_room()
        elif self._player.get_current_location() == self._rooms[17]:
            self.handle_study()

    def handle_cellar(self):
        if self._user_input.upper() == "FORGIVE":
            print(f"\n{self._rooms[self._player.get_current_location()].get_ending_1()}")
            return False
        else:
            print(f"\n{self._rooms[self._player.get_current_location()].get_ending_2()}")
            return False
    
    def handle_den(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_dining_room(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "KITCHEN":
            self._player.set_current_room(self._rooms[5])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_foyer_closet(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "UMBRELLA":
            self._player.add_inventory_item("umbrella", True)
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_foyer(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DOOR":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        elif self._user_input.upper() == "CELLAR":
            if self._player.get_item_value("key_cellar"):
                self._player.set_current_room(self._rooms[0])
            else:
                print(f"\nYou lack the required item(s). ")
        elif self._user_input.upper() == "DEN":
            self._player.set_current_room(self._rooms[1])
        elif self._user_input.upper() == "DINING ROOM":
            self._player.set_current_room(self._rooms[2])
        elif self._user_input.upper() == "FOYER CLOSET":
            self._player.set_current_room(self._rooms[3])
        elif self._user_input.upper() == "STAIRCASE":
            self._player.set_current_room(self._rooms[7])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_kitchen(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "PANTRY":
            self._player.set_current_room(self._rooms[6])
        elif self._user_input.upper() == "KNIFE":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_pantry(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_staircase(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "LANDING":
            self._player.set_current_room(self._rooms[13])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bathroom(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bedroom_1(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bedroom_2(self):
        # ["EXIT", "CAGE"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "CAGE":
            if self._player.get_item_value("knife"):
                print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
                self._player.add_item_inventory("key_mb", True)
            else:
                print(f"\nYou lack the required item(s). ")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_hall_1(self):
        # ["BATHROOM", "LEFT BEDROOM", "RIGHT BEDROOM", "STUDY", "EXIT", "HALLWAY"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "BATHROOM":
            self._player.set_current_room(self._rooms[8])
        elif self._user_input.upper() == "LEFT BEDROOM":
            self._player.set_current_room(self._rooms[9])
        elif self._user_input.upper() == "RIGHT BEDROOM":
            self._player.set_current_room(self._rooms[10])
        elif self._user_input.upper() == "STUDY":
            self._player.set_current_room(self._rooms[17])
        elif self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(self._rooms[12])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_hall_2(self):
        # ["MUSIC ROOM", "MASTER BEDROOM", "EXIT"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "MUSIC ROOM":
            self._player.set_current_room(self._rooms[16])
        elif self._user_input.upper() == "MASTER BEDROOM":
            self._player.set_current_room(self._rooms[15])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_landing(self):
        # ["EXIT", "HALLWAY"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(self._rooms[11])
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_master_bath(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_master_bed(self):
        # ["EXIT", "MASTER BATH", "KEY"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "MASTER BATH":
            self._player.set_current_room(self._rooms[14])
        elif self._user_input.upper() == "KEY":
            if self._player.get_item_value("umbrella"):
                print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
                self._player.add_item_inventory("key_cellar", True)
            else:
                print(f"\nYou lack the required item(s). ")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_music_room(self):
        # ["EXIT", "DESK"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DESK":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_study(self):
        # ["EXIT", "DESK"]
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DESK":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
            self._player.add_item_inventory("magnifying glass", True)
        else:
            print(f"\nI'm sorry I don't understand. ")