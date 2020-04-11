#!/usr/bin/python3
"""
    This program filters all words in the list and it does this with the following procedure:

    Words that have one or more of these specifications will be deleted from the list:
    - Words with more than 7 different letters
    - Words with a less than 4 letters in length
    - Words with digits in them
    - Words with punctuation
    - Words that have an uppercase letter as their first letter (proper nouns)
    - Words with superscript or subscript
    - swearwords(cussing) (will be in another list to filter them out of the usefull words)

    Words that we are going to change:
    - Words with 1 or more accents, for example: ë é
      (The letter will be changed to the same letter without the accent(s)
    - Words that have an uppercase letter which is not their first letter
      (Will be changed to the same word but lowercase)
"""
import string
import unidecode
from pathlib import Path


def pangrams():
    """
    This function returns perfect pangrams from the 7 letters that are on screen
    :return: all perfect pangrams that are possible with the 7 letters on screen
    """
    words = filter_list
    return {word for word in words if len(word) == 7 and len(set(word)) == 7}


def pangrams_only(letters_on_display):
    """
    This function returns pangrams from the 7 letters that are on screen
    :param: The 7 seven letters that are on display in the game
    :return: all pangrams that are possible with the 7 letters on screen
    """
    words_possible = possible_words(letters_on_display)
    letters_on_display = list(letters_on_display)
    almost_perfect_pangrams = []
    for word in words_possible:
        counter = 0
        for letter in letters_on_display:
            if letter not in word:
                break
            else:
                counter = counter + 1
                if counter == len(letters_on_display):
                    if len(word) == 7:
                        almost_perfect_pangrams.append(word)
    return set(almost_perfect_pangrams)


def possible_words(letters_on_display):
    """
    This function returns every word that could be guessed with the 7 letters on screen that has the middle letter,
    and isn't filtered out already
    :param: The 7 seven letters that are on display in the game
    :return: all verified words that can be made from the 7 letters on screen.
    """
    words_set = filter_list  # hier roept ie dus dat andere programma aan en krijgt ie de woordenlijst van alle
    # mogelijke woorden, voor alle letters van het alfabet
    good_words = []
    for word in words_set:
        counter = 0
        for car in word:
            if car not in letters_on_display:
                break
            counter += 1
            # gaat net zo lang door totdat er break is voor het woord en anders net zo lang totdat alle chars zijn
            # geweest

            if len(word) == counter and letters_on_display[0] in word:
                good_words.append(word)
        # zijn alle chars geweest, dus heeft het algo bevestigd dat alle chars in de letters_on_display zaten dan
        # voegt hij hem hier toe

    return good_words


def filter():
    """
    This function takes the words_list and cusswords and cleans the words in the words_list,
    till they are good enough to use for words in the spelling bee. The outcome is every possible word,
    that could be guessed en would be right.
    :return: set with all words that fulfill the needs of the spelling bee rules
    """
    words, curse_words = get_files()

    exceptions = string.punctuation + string.digits + " \t\xb2\xb3\u2082\xb4"
    # punctuation, superscript, subscript, digits

    clean_list = [word.replace('\n', "") for word in words if not any(p in word for p in exceptions)]
    # haalt hier de enters uit elk element en checkt op de exceptions

    clean_list = {unidecode.unidecode(word) for word in clean_list if len(word) >= 4 and not word[0] == word[0].upper()}
    # Eerste letter een hoofdletter, lengte van woord, accenten

    better_words = set()
    for word in clean_list:
        letters_in_word = {char for char in word}
        if len(letters_in_word) < 8:
            better_words.add(word)
    letters_in_word = {}
    # woorden met meer dan 7 verschillende letters

    return better_words - curse_words


def get_files():
    """
    This function gets data from woorden.txt in the from of normal Dutch words
    and it gets data from scheldwoorden.txt in the form of Dutch cusswords.
    :return: 2 sorts of data as in a wordlist with normal words and a list with cusswords
    """
    woorden_path = Path(__file__).parent / "woorden.txt"
    scheldwoorden_path = Path(__file__).parent / "scheldwoorden.txt"
    with open(woorden_path, 'r', encoding='utf-8') as w:
        data = w.readlines()
    with open(scheldwoorden_path, 'r', encoding='utf-8') as s:
        scheldwoorden = set(s.readlines())
    return data, scheldwoorden


filter_list = filter()
# This is a global variable used for storing the filtered list.
# Once someone presses new hive, the system will not execute the whole filter again,
# but it will just go to this variable where the list is already stored (saves lots of time).


def main():
    pass


if __name__ == "__main__":
    main()
