"""
Wat dit programma doet is het pakt de 7 letters die in de hive staan en geeft een combinatie van deze letters terug

"""

from random import *
from Gamestate import GameState
from woordenlijst.woordenlijst_filter import possible_words


def find_match(letters):
    """
    Deze functie gaat net zo lang door totdat de guess een daadwerkelijk bestaand woord is.
    :param: The 7 letters that are on screen when playing the game
    :return: A guess that is actually in the list, so a right guessed guess
    """
    # possible_words zijn hier de woorden die je mogelijk kunt maken met de 7 letters
    guess = []
    while guess not in possible_words(letters):
        guess = give_guess(letters)
    return print(guess)


def give_guess(letters):
    """
    This function returns a guess that could possibly be a word in the list of possible_words
    :param: The 7 letters that are on screen when playing the game
    :return: returns a guess
    """
    if random() < 0.8:                          # the change that a word has 10 or more letters is very small so,
        amount_of_letters = randint(4, 11)      # to make the system faster i gave it 20% change to be a large word.
    else:
        amount_of_letters = randint(10, 22)
    guess = [choice(letters) for i in range(amount_of_letters)]
    if letters[0] not in guess:                 # Middle letter of hive has to be in guess (in this case letters[0])
        guess.extend(letters[0])
        shuffle(guess)
    return "".join(guess)


def main():
    gamestate = GameState()
