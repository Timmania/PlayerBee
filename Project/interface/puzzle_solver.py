"""
Wat dit programma doet is het pakt de 7 letters die in de hive staan en geeft een combinatie van deze letters terug

"""

from random import *
from Gamestate import GameState
from woordenlijst.woordenlijst_filter import possible_words


def find_match(letters):
    """
    Deze functie gaat net zo lang door totdat de guess een daadwerkelijk bestaand woord is.

    """
    # possible_words zijn hier de woorden die je mogelijk kunt maken met de 7 letters
    guess = []
    while guess not in possible_words(letters):
        guess = give_guess(letters)
    return print(guess)


def give_guess(letters):
    """
    Deze functie neemt de letters in de hive en geeft met deze letters een guess in deze voor de letters in deze hive

    """
    if random() < 0.8:
        amount_of_letters = randint(4, 11)
    else:
        amount_of_letters = randint(10, 22)
    guess = [choice(letters) for i in range(amount_of_letters)]
    if letters[0] not in guess:
        guess.extend(letters[0])
        shuffle(guess)
    return "".join(guess)



def main():
    gamestate = GameState()
