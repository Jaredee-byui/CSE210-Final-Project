visit_status_initial = False

cellar_intro = r"escape\game\rooms\ground_floor\ground_floor_text\cellar_intro_1.txt"
cellar_ending_3 = r"escape\game\rooms\ground_floor\ground_floor_text\cellar_joke_end.txt"
cellar_ending_1 = r"escape\game\rooms\ground_floor\ground_floor_text\cellar_good_end.txt"
cellar_ending_2 = r"escape\game\rooms\ground_floor\ground_floor_text\cellar_bad_end.txt"
cellar_adjacent = ["foyer"]
cellar_actions = ["FORGIVE"]

den_intro = r"escape\game\rooms\ground_floor\ground_floor_text\den_intro_1.txt"
den_adjacent = ["foyer"]
den_actions = ["EXIT"]

dining_intro = r"escape\game\rooms\ground_floor\ground_floor_text\dining_room_intro_1.txt"
dining_adjacent = ["foyer", "kitchen"]
dining_actions = ["EXIT", "KITCHEN"]

foyer_closet_intro = r"escape\game\rooms\ground_floor\ground_floor_text\foyer_closet_intro_1.txt"
foyer_closet_umbrella = r"escape\game\rooms\ground_floor\ground_floor_text\foyer_closet_umbrella.txt"
foyer_closet_adjacent = ["foyer"]
foyer_closet_actions = ["EXIT", "UMBRELLA"]

foyer_intro = r"escape\game\rooms\ground_floor\ground_floor_text\foyer_intro_1.txt"
foyer_door = r"escape\game\rooms\ground_floor\ground_floor_text\foyer_door.txt"
foyer_adjacent = ["cellar", "den", "dining_room", "foyer_closet", "staircase"]
foyer_actions = ["DOOR", "CELLAR", "DEN", "DINING ROOM", "FOYER CLOSET", "STAIRCASE"]

kitchen_intro = r"escape\game\rooms\ground_floor\ground_floor_text\kitchen_intro_1.txt"
kitchen_knife = r"escape\game\rooms\ground_floor\ground_floor_text\kitchen_knife.txt"
kitchen_adjacent = ["dining_room", "pantry"]
kitchen_actions = ["EXIT", "PANTRY", "KNIFE"]

pantry_intro = r"escape\game\rooms\ground_floor\ground_floor_text\pantry_intro_1.txt"
pantry_adjacent = ["dining_room"]
pantry_actions = ["EXIT"]

staircase_intro = r"escape\game\rooms\ground_floor\ground_floor_text\staircase_intro_1.txt"
staircase_adjacent = ["foyer", "landing"]
staircase_actions = ["EXIT", "LANDING"]

bathroom_intro = r"escape\game\rooms\upper_floor\upper_floor_text\bathroom_intro_1.txt"
bathroom_adjacent = ["hall_1"]
bathroom_actions = ["EXIT"]

bedroom_1_intro = r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_1_intro_1.txt"
bedroom_1_adjacent = ["hall_1"]
bedroom_1_actions = ["EXIT"]

bedroom_2_intro = r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_2_intro_1.txt"
bedroom_2_puzzle = r"escape\game\rooms\upper_floor\upper_floor_text\bedroom_2_puzzle_action.txt"
bedroom_2_adjacent = ["hall_1"]
bedroom_2_actions = ["EXIT", "CAGE"]

hall_1_intro = r"escape\game\rooms\upper_floor\upper_floor_text\hall_1_intro_1.txt"
hall_1_adjacent = ["bathrom", "bedroom_1", "bedroom_2", "study"]
hall_1_actions = ["BATHROOM", "LEFT BEDROOM", "RIGHT BEDROOM", "STUDY", "EXIT", "HALLWAY"]

hall_2_intro = r"escape\game\rooms\upper_floor\upper_floor_text\hall_2_intro_1.txt"
hall_2_adjacent = ["music_room", "master_bed"]
hall_2_actions = ["MUSIC ROOM", "MASTER BEDROOM", "EXIT"]

landing_intro = r"escape\game\rooms\upper_floor\upper_floor_text\landing_intro_1.txt"
landing_adjacent = ["hall_1", "staircase"]
landing_actions = ["EXIT", "HALLWAY"]

master_bath_intro = r"escape\game\rooms\upper_floor\upper_floor_text\master_bath_intro_1.txt"
master_bath_adjacent = ["master_bed"]
master_bath_actions = ["EXIT"]

master_bed_intro = r"escape\game\rooms\upper_floor\upper_floor_text\master_bed_intro_1.txt"
master_bed_key = r"escape\game\rooms\upper_floor\upper_floor_text\master_bed_puzzle.txt"
master_bed_adjacent = ["hall_2", "master_bath"]
master_bed_actions = ["EXIT", "MASTER BATH", "KEY"]

music_room_intro = r"escape\game\rooms\upper_floor\upper_floor_text\music_room_intro_1.txt"
music_room_book_1 = r"escape\game\rooms\upper_floor\upper_floor_text\music_room_book.txt"
# music_room_book_2 = r"escape\game\rooms\upper_floor\upper_floor_text\music_room_book_2.txt"
music_room_adjacent = ["hall_2"]
music_room_actions = ["EXIT", "DESK"]

study_intro = r"escape\game\rooms\upper_floor\upper_floor_text\study_intro_1.txt"
study_desk = r"escape\game\rooms\upper_floor\upper_floor_text\search_desk.txt"
study_adjacent = ["hall_1"]
study_actions = ["EXIT", "DESK"]


