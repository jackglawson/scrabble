from dataclasses import dataclass


@dataclass(frozen=True)
class Params:
    starting_letters = {'A': 13, 'B': 3, 'C': 3, 'D': 6, 'E': 18, 'F': 3,
                        'G': 4, 'H': 3, 'I': 12, 'J': 2, 'K': 2, 'L': 5,
                        'M': 3, 'N': 8, 'O': 11, 'P': 3, 'Q': 2, 'R': 9,
                        'S': 6, 'T': 9, 'U': 6, 'V': 3, 'W': 3, 'X': 2,
                        'Y': 3, 'Z': 2}

    initial_grid_size = 21

    num_starting_tiles = 10
    peel_size = 2

    lexicon_filename = "lexicon.txt"


p = Params()
