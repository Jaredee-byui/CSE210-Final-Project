from game import constants
from game import room
from game.room import Room
from game import player
from game.game_logic import GameLogic

class Director:
    def __init__(self, rooms, player):
        self._rooms = rooms
        self._player = player
        self._keep_playing = True
        self._game_logic = GameLogic()
        

    def start_game(self):
        starting_room = self._rooms[4]
        self._player.set_current_room(starting_room)

        while self._keep_playing:
            self.play_room_intro()
            self.get_input()
            self.update_game()

    def play_room_intro(self):
        print(f"\n{self._rooms[self._player.get_current_location()].get_room_intro()}")
        

    def get_input(self):
        valid_input = False
        while valid_input:
            self._user_input = input("What would you like to do?")
            try:
                self._user_input.upper()
            except:
                valid_input = False
        


    def update_game(self):
        pass
