"""
Wat dit programma doet is het pakt de 7 letters die in de hive staan en geeft een combinatie van deze letters terug

"""

from random import *


def find_match(letters_in_hive):
    """
    Deze functie gaat net zo lang door totdat de guess een daadwerkelijk bestaand woord is.

    """
    guess = []
    while guess not in possible_words:              # possible_words zijn hier de woorden die je mogelijk kunt maken met de 7 letters
        guess = give_guess(letters_in_hive)
    return guess


def give_guess(letters_in_hive):
    """
    Deze functie neemt de letters in de hive en geeft met deze letters een guess in deze voor de letters in deze hive

    """
    # letters_in_hive is een list, set, tuple of dictionary
    if random() < 0.8:
        amount_of_letters = randint(4, 11)
    else:
        amount_of_letters = randint(10, 22)
    return [choice(letters_in_hive) for i in range(amount_of_letters)]
