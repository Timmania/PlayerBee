from woordenlijst.woordenlijst_filter import *
import random


class GameState:
    def __init__(self):
        self.letters = []
        self.score = 0
        self.word_set = set()  # possible_words(self.letters)
        self.guesses = set()
        self.pangram_set = pangrams()

    def reset_game(self):
        """
        Gets a new random pangram, removes it from the pangram list and
        shuffles the pangram's letters to get a new list of letters
        :return: nothing as it calls a new set command
        """
        new = random.sample(self.pangram_set, 1)[0]

        self.pangram_set.remove(new)
        new = list(new)
        random.shuffle(new)
        self.letters = new
        self.set_words()
        self.guesses = set()

    def set_words(self):
        """
        Gets all the possible words from woordenlijst_filter.py
        using the letter array and takes all words from that list
        that include the first letter of the array
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
        if word == "all_found":
            self.score += 20
            return "Graat voltooid! +20"
        if len(word) == 4:
            self.score += 1
            return ["+1", 1]
        elif sorted(list(set(list(word)))) == sorted(self.letters):
            self.score += len(word) + 7
            return ["PANGRAM GEVONDEN! +" + str(len(word) + 7), len(word) + 7]
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
        if guess in self.guesses:
            return ["Woord al gereden"]
        else:
            self.guesses.add(guess)

        if len(guess) < 4:
            return ["Woordlengte minimaal 4 letters"]
        if not all(x in self.letters for x in list(guess)):
            return ["Gegeven letter niet in graat"]
        if not self.letters[0] in guess:
            return ["Middelste letter niet gebruikt"]
        if guess not in self.word_set:
            return ["Gegeven woord niet gevonden"]

        self.word_set.remove(guess)
        return self.increase_score(guess)

    def get_hint(self):
        """
        Gives user hint
        :return: first two letters of a unguessed word
        """
        hint = random.sample(self.word_set, 1)[0]
        return [hint[:2], len(hint) - 2]

