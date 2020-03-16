from woordenlijst.woordenlijst_filter import *
import random


class GameState:
    def __init__(self):
        self.letters = []  # TODO dit moet gefixed worden
        self.score = 0
        self.word_set = set()  # possible_words(self.letters)
        self.pangram_set = pangrams()

        self.set_letters()  # TODO dit moet ook gefixed worden

    def set_letters(self):
        """
        Gets a new random pangram, removes it from the pangram list and shuffles the pangram's letters
        to get a new list of letters

        :return: nothing as it calls a new set command
        """
        new = random.choice(self.pangram_set)
        self.pangram_set.remove(new)
        new = [ch for ch in new]
        self.letters = random.shuffle(new)
        self.set_words()

    def set_words(self):
        """
        Gets all the possible words from woordenlijst_filter.py using the letter array
        and takes all words from that list that include the first letter of the array
        """
        words = possible_words(self.letters)
        self.word_set = {word for word in words if self.letters[0] in word}

    def increase_score(self, word):
        """
        Increases the score in 3 ways
        4 letter words get 1 point
        a pangram gets 14 points
        any other guess gets points based on the length of the guess
        :param word: correct guess
        :return: list with message and score as integer
        """
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
        """
        Checks if the guess is a correct guess, if not the player gets feedback
        otherwise your score increases
        :param guess: user input
        :return: list with user feedback or call to increase_score
        """
        if len(guess) < 4:
            return ["Word must be 4 letters minimum"]
        if not all(x in self.letters for x in list(guess)):
            return ["Letter not in grate"]
        if not self.letters[0] in guess:
            return ["Middle letter not in guess"]
        if guess not in self.word_set:
            return ["Word not in word set"]
        return self.increase_score(guess)
