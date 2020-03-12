from woordenlijst.woordenlijst_filter import *
import random


class GameState:
    def __init__(self):
        self.letters = ["a", "e", "p", "g", "n", "r", "l"]  # TODO dit moet gefixed worden
        self.score = 0
        self.word_set = possible_words(self.letters)
        self.pangram_set = list({"alrhxie", "ajdfndo", "akrpche", "ahrpelc"})  # TODO dit moet gefixed worden
        # self.set_letters()  # TODO dit moet ook gefixed worden

    def get_score(self):
        return self.score

    def get_letters(self):
        return self.letters

    def set_letters(self):
        new = random.choice(self.pangram_set)
        self.pangram_set.remove(new)
        new = [ch for ch in new]
        self.letters = new
        return new

    def increase_score(self, word):
        if len(word) == 4:
            self.score += 1
            return ["+1", 1]
        elif sorted(list(word)) == sorted(self.letters):
            self.score += 14
            return ["PANGRAM FOUND! +14", len(word)]
        else:
            self.score += len(word)
            return ["+" + str(len(word)), len(word)]

    def is_correct(self, guess):
        if len(guess) < 4:
            return ["Word must be 4 letters minimum"]
        if not all(x in self.letters for x in list(guess)):
            return ["Letter not in grate"]
        if not self.letters[0] in guess:
            return ["Middle letter not in guess"]
        if guess not in self.word_set:
            return ["Word not in word set"]
        return self.increase_score(guess)
