from game.director import Director
from game.room import Room
from game import constants
from game.player import Player

def main():
    player = Player()
    rooms = []
    # self, visit_status, intro_1, unique_text, ending_1, ending_2, adjacent_rooms, actions)
    cellar = Room(False, constants.cellar_intro, constants.cellar_ending_3, constants.cellar_ending_1, constants.cellar_ending_2, constants.cellar_adjacent, constants.cellar_actions)
    rooms.append(cellar)
    den = Room(False, constants.den_intro, " ", " ", " ", constants.dining_adjacent, constants.den_actions)
    rooms.append(den)
    dining_room = Room(False, constants.dining_intro, " ", " ", " ", constants.dining_adjacent, constants.foyer_actions)
    rooms.append(dining_room)
    foyer_closet = Room(False, constants.foyer_closet_intro, constants.foyer_closet_umbrella, " ", " ", constants.foyer_closet_adjacent, constants.foyer_closet_actions)
    rooms.append(foyer_closet)
    foyer = Room(False, constants.foyer_intro, constants.foyer_door, " ", " ", constants.foyer_adjacent, constants.foyer_actions)
    rooms.append(foyer)
    kitchen = Room(False, constants.kitchen_intro, constants.kitchen_knife, " ", " ", constants.kitchen_adjacent, constants.kitchen_actions)
    rooms.append(kitchen)
    pantry = Room(False, constants.pantry_intro, " ", " ", " ", constants.pantry_adjacent, constants.pantry_actions)
    rooms.append(pantry)
    staircase = Room(False,constants.staircase_intro, " ", " ", " ", constants.staircase_adjacent, constants.staircase_actions)
    rooms.append(staircase)
    bathroom = Room(False, constants.bathroom_intro, " ", " ", " ", constants.bathroom_adjacent, constants.bathroom_actions)
    rooms.append(bathroom)
    bedroom_1 = Room(False, constants.bedroom_1_intro, " ", " ", " ", constants.bedroom_1_adjacent, constants.bedroom_1_actions)
    rooms.append(bedroom_1)
    bedroom_2 = Room(False, constants.bedroom_2_intro, constants.bedroom_2_puzzle, " ", " ", constants.bedroom_2_adjacent, constants.bedroom_2_actions)
    rooms.append(bedroom_2)
    hall_1 = Room(False, constants.hall_1_intro, " ", " ", " ", constants.hall_1_adjacent, constants.hall_1_actions)
    rooms.append(hall_1)
    hall_2 = Room(False, constants.hall_2_intro, " ", " ", " ", constants.hall_2_adjacent, constants.hall_2_actions)
    rooms.append(hall_2)
    landing = Room(False, constants.landing_intro, " ", " ", " ", constants.landing_adjacent, constants.landing_actions)
    rooms.append(landing)
    master_bath = Room(False, constants.master_bath_intro, " ", " ", " ", constants.master_bath_adjacent, constants.master_bath_actions)
    rooms.append(master_bath)
    master_bed = Room(False, constants.master_bed_intro, constants.master_bed_key, " ", " ", constants.master_bed_adjacent, constants.master_bed_actions)
    rooms.append(master_bed)
    music_room = Room(False, constants.music_room_intro, constants.music_room_book_1, " ", " ", constants.music_room_adjacent, constants.music_room_actions)
    rooms.append(music_room)
    study = Room(False, constants.study_intro, constants.study_desk, " ", " ", constants.study_adjacent, constants.study_actions)
    rooms.append(study)


    director = Director(rooms, player)
    director.start_game()



if __name__ == "__main__":
    main()