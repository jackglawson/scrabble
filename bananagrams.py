from copy import copy
import random
import numpy as np

from trie import Trie
from params import p


def load_trie():
    lexicon_file = open(p.lexicon_filename, 'r')
    lexicon = [line.rstrip() for line in lexicon_file.readlines()]
    trie = Trie()
    trie.add_words(lexicon)
    return trie


class Bananagrams:
    def __init__(self):
        self.bunch = copy(p.starting_letters)
        self.num_remaining_tiles = sum(p.starting_letters.values())

        self.my_tiles = []

        self.grid = np.array([['-'] * p.initial_grid_size for _ in range(p.initial_grid_size)])
        self.trie = load_trie()

    def _take_letters(self, n):
        assert sum(self.bunch.values()) >= n, "Out of letters!"
        for _ in range(n):
            new_letter = random.choices(list(self.bunch.keys()), weights=self.bunch.values())[0]
            self.bunch[new_letter] -= 1
            self.num_remaining_tiles -= 1
            self.my_tiles.append(new_letter)

    def _increase_grid_size(self, direction: str):
        """Direction can be one of (l, r, u, d)"""
        height = len(self.grid)
        width = len(self.grid[0])

        if direction == "l":
            new_grid = np.array([['-'] * (width + 1) for _ in range(height)])
            new_grid[:, 1:] = self.grid
        elif direction == "r":
            new_grid = np.array([['-'] * (width + 1) for _ in range(height)])
            new_grid[:, :-1] = self.grid
        elif direction == "u":
            new_grid = np.array([['-'] * width for _ in range(height + 1)])
            new_grid[1:, :] = self.grid
        elif direction == "d":
            new_grid = np.array([['-'] * width for _ in range(height + 1)])
            new_grid[:-1, :] = self.grid
        else:
            raise Exception("invalid grid direction")

        self.grid = new_grid

    def _place_best_word(self):
        # Find available tiles
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j] == "-":
                    continue
                else:


    def play(self):
        # place highest scoring words
        # if cant get a word longer than c, remove the last word and try again


        self._take_letters(p.num_starting_tiles)

        while self.num_remaining_tiles > 0:






    def __repr__(self):
        return '\n'.join([' '.join(row) for row in self.grid])
