from game.director import Director
from game.room import Room
from game import constants
from game.player import Player


def main():
    player = Player()
    rooms = []
    # self, visit_status, intro_1, unique_text, ending_1, ending_2, adjacent_rooms, actions)
    cellar = Room(constants.cellar_intro, constants.cellar_ending_3, constants.cellar_ending_1, constants.cellar_ending_2)
    rooms.append(cellar)
    den = Room(constants.den_intro, " ", " ", " ")
    rooms.append(den)
    dining_room = Room(constants.dining_intro, " ", " ", " ")
    rooms.append(dining_room)
    foyer_closet = Room(constants.foyer_closet_intro, constants.foyer_closet_umbrella, " ", " ")
    rooms.append(foyer_closet)
    foyer = Room(constants.foyer_intro, constants.foyer_door, " ", " ")
    rooms.append(foyer)
    kitchen = Room(constants.kitchen_intro, constants.kitchen_knife, " ", " ")
    rooms.append(kitchen)
    pantry = Room(constants.pantry_intro, " ", " ", " ")
    rooms.append(pantry)
    staircase = Room(False,constants.staircase_intro, " ", " ", " ")
    rooms.append(staircase)
    bathroom = Room(constants.bathroom_intro, " ", " ", " ")
    rooms.append(bathroom)
    bedroom_1 = Room(constants.bedroom_1_intro, " ", " ", " ")
    rooms.append(bedroom_1)
    bedroom_2 = Room(constants.bedroom_2_intro, constants.bedroom_2_puzzle, " ", " ")
    rooms.append(bedroom_2)
    hall_1 = Room(constants.hall_1_intro, " ", " ", " ")
    rooms.append(hall_1)
    hall_2 = Room(constants.hall_2_intro, " ", " ", " ")
    rooms.append(hall_2)
    landing = Room(constants.landing_intro, " ", " ", " ")
    rooms.append(landing)
    master_bath = Room(constants.master_bath_intro, " ", " ", " ")
    rooms.append(master_bath)
    master_bed = Room(constants.master_bed_intro, constants.master_bed_key, " ", " ")
    rooms.append(master_bed)
    music_room = Room(constants.music_room_intro, constants.music_room_book_1, " ", " ")
    rooms.append(music_room)
    study = Room(constants.study_intro, constants.study_desk, " ", " ")
    rooms.append(study)

    director = Director(rooms, player)
    director.start_game()



if __name__ == "__main__":
    main()