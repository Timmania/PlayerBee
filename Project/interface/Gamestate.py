# from woordenlijst import word_set


class GameState:
    def __init__(self):
        self.letters = ["b", "p", "l", "a", "y", "e", "r"]
        self.score = 0
        self.word_set = {}

    def get_letters(self):
        return self.letters

    def set_letters(self, letters):
        self.letters = letters

    def increase_score(self, word):
        if len(word) == 4:
            self.score += 1
        elif len(word):
            pass

    def is_correct(self, guess):
        if not all(x in self.letters for x in list(guess)):
            return "Letter not in grate"
        if not self.letters[0] in guess:
            return "Middle letter not in guess"
        if guess not in self.word_set:
            return "Word not in word set"
        return True
