
class Const:


# Distribution of players
    PLAYERS_PER_ISLAND = 10
    MIN_BOTS_PER_ISLAND = 0
    MAX_HUMANS_PER_ISLAND = 6

# Game constants
    PHASES_PER_GAME = 50
    STARTING_SCORE = 0
    NB_RUNS_FOR_STATS = 20

# Misc constants
    RANDOM_ID_LEN = 3

# Score given to survivors
    SCORE_FOR_TRIAL = 3
    SCORE_FOR_LASTMAN = 20
    SCORE_FOR_EACH_TRAITOR = 1
    SCORE_FOR_ALL_TRAITORS = 20

    INSTANCES_STRENGTH = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    INSTANCES_PER_PLAYER = len(INSTANCES_STRENGTH)
    DIFFICULTY_A = 40           # actual difficulty is A*n + B where n is the number of remaining players
    DIFFICULTY_B = 20
