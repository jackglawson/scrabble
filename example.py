from trie import Trie
from copy import copy
import random
import time

s = time.time()

filename = 'lexicon.txt'
lexicon_file = open(filename, 'r')
lexicon = [line.rstrip() for line in lexicon_file.readlines()]
trie = Trie()
trie.add_words(lexicon)


LETTER_DISTRIBUTION = {'A': 13, 'B': 3, 'C': 3, 'D': 6, 'E': 18, 'F': 3,
                       'G': 4, 'H': 3, 'I': 12, 'J': 2, 'K': 2, 'L': 5,
                       'M': 3, 'N': 8, 'O': 11, 'P': 3, 'Q': 2, 'R': 9,
                       'S': 6, 'T': 9, 'U': 6, 'V': 3, 'W': 3, 'X': 2,
                       'Y': 3, 'Z': 2}


def take_letters(n):
    remaining_letters = copy(LETTER_DISTRIBUTION)

    letters = []
    for _ in range(n):
        new_letter = random.choices(list(remaining_letters.keys()), weights=remaining_letters.values())[0]
        letters.append(new_letter)
        remaining_letters[new_letter] -= 1
    return letters


if __name__ == "__main__":
    print("Loaded Trie in {} seconds.".format(round(time.time() - s, 3)))
    while True:
        print("Please input letters to be descrambled. No separation required.")
        print("Alternatively, input an integer, n, to randomly pick n letters from a bag of 144 letters")
        i = input()

        if i.isalpha():
            letters = list(i.upper())
        elif i.isnumeric():
            n = int(i)
            letters = take_letters(n)
        else:
            print("Invalid input! Please try again. ")
            continue

        s = time.time()
        words = trie.find_words(letters)
        f = time.time()

        longest_words = [w for w in words if len(w) == len(max(words, key=len))]

        print("{} words found in {} seconds".format(len(words), f-s))
        print("The longest word length is {}: ".format(len(longest_words[0])))
        for w in longest_words:
            print("   ", w.capitalize())
        print("\n")

        again = input("Would you like to descramble more letters? (y/n) ")

        if again == "y":
            continue
        else:
            print("Quitting")
            break
