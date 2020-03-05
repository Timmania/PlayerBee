# from woordenlijst import word_set
import random


class GameState:
    def __init__(self):
        self.letters = []
        self.score = 0         # TODO create function to get score
        self.word_set = set()  # TODO link to wordlist to get set of words with self.letters
        self.pangram_set = set()

        self.set_letters()

    def get_letters(self):
        return self.letters

    def set_letters(self):
        new = random.choice(self.pangram_set)
        self.pangram_set.remove(new)
        self.letters = new

    def increase_score(self, word):
        if len(word) == 4:
            self.score += 1
            return "+1"
        elif sorted(list(word)) == sorted(self.letters):
            self.score += 14
            return "PANGRAM FOUND! +14"
        else:
            self.score += len(word)
            return "+" + str(len(word))

    def is_correct(self, guess):
        if not all(x in self.letters for x in list(guess)):
            return "Letter not in grate"
        if not self.letters[0] in guess:
            return "Middle letter not in guess"
        if guess not in self.word_set:
            return "Word not in word set"
        return self.increase_score(guess)
