
class Const:


# Distribution of players
    PLAYERS_PER_ISLAND = 12
    MIN_BOTS_PER_ISLAND = 0
    MAX_HUMANS_PER_ISLAND = PLAYERS_PER_ISLAND

# Game constants
    PHASES_PER_GAME = 100
    STARTING_SCORE = 0
    NB_RUNS_FOR_STATS = 10

# Misc constants
    RANDOM_ID_LEN = 10

# Score given to survivors
    SCORE_FOR_TRIAL = 3
    SCORE_FOR_LASTMAN = 100
    SCORE_FOR_EACH_TRAITOR = 0
    SCORE_FOR_ALL_TRAITORS = 100

    INSTANCES_STRENGTH = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    INSTANCES_PER_PLAYER = len(INSTANCES_STRENGTH)
    DIFFICULTY_A = 7           # actual difficulty is A*n + B where n is the number of remaining players
    DIFFICULTY_B = -3

    AI_TUNE = [ [-30, 30, 2],
                [-3, 3, 3],
                [-3, 30, 3],
                [-30, 3, 3],
                [-30, 30, 3],
            ]