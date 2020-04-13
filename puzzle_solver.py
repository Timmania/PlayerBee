"""
    This program tries to solve the puzzle, 1 word at the time.
    It stops when it actually found 1 word. It prints that word on the screen.
"""
import sys
from random import *
from woordenlijst.woordenlijst_filter import possible_words


def find_match(letters):
    """
    This function goes on until a guess from give_guess is actually a good one.
    When it is a good one it prints it on screen.
    :param: The 7 letters that are on screen when playing the game
    :return: A guess that is actually in the list, so a right guessed guess
    """
    # possible_words are the words that you can possibly make
    # with the 7 letters on screen when playing
    guess = []
    while guess not in possible_words(letters):
        guess = give_guess(letters)
    print(guess)


def give_guess(letters):
    """
    This function returns a guess that could possibly be a word
    in the list of possible_words.
    :param: The 7 letters that are on screen when playing the game
    :return: returns a guess
    """
    if random() < 0.8:
        # the change that a word has or more letters is very small so,
        amount_of_letters = randint(4, 11)
        # to make the system faster i gave it 20% change to be a large word.
    else:
        amount_of_letters = randint(10, 22)
    guess = [choice(letters) for i in range(amount_of_letters)]
    if letters[0] not in guess:
        # Middle letter of hive has to be in guess (in this case letters[0])
        guess.extend(letters[0])
        shuffle(guess)
    return "".join(guess)
    # returns guess as string


def main(argv):
    if len(argv) != 8:
        print("Usage: python puzzle_solver.py letter1 letter2 etc...")
        exit(0)
    _, x1, x2, x3, x4, x5, x6, x7 = argv
    letters = [x1, x2, x3, x4, x5, x6, x7]

    find_match(letters)


if __name__ == '__main__':
    main(sys.argv)