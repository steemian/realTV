
class Const:


# Distribution of players
    PLAYERS_PER_ISLAND = 10
    MIN_BOTS_PER_ISLAND = 0

# Game constants
    PHASES_PER_GAME = 20
    STARTING_SCORE = 0

# Misc constants
    RANDOM_ID_LEN = 10

# Score given to survivors
    SCORE_FOR_TRIAL = 1
    SCORE_FOR_LASTMAN = 10
    SCORE_FOR_TRAITOR = 1

    INSTANCES_STRENGTH = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    DIFFICULTY_A = 50           # actual difficulty is A*n + B where n is the number of remaining players
    DIFFICULTY_B = 30
