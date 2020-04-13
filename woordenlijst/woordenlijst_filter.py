#!/usr/bin/python3
"""
This program filters all words in the list and it does this with
the following procedure:

    Words that have one or more of these specifications will be deleted
    from the list:
    - Words with more than 7 different letters
    - Words with a less than 4 letters in length
    - Words with digits in them
    - Words with punctuation
    - Words that have an uppercase letter as their first letter (proper nouns)
    - Words with superscript or subscript
    - swearwords(cussing)
    (will be in another list to filter them out of the usefull words)

    Words that we are going to change:
    - Words with 1 or more accents, for example: ë é
      (The letter will be changed to the same letter without the accent(s)
    - Words that have an uppercase letter which is not their first letter
      (Will be changed to the same word but lowercase)

This program also gives the words that are possible,
with the 7 letters on screen (which include the middle letter).
And it gives pangrams which can be made with the 7 letters on screen.

"""
import string
import unidecode
from pathlib import Path


def pangrams():
    """
    This function returns pangrams from the 7 letters that are on screen
    :return: pangrams that are possible with the 7 letters on screen
    """
    words = filter_list
    return {word for word in words if len(word) == 7 and len(set(word)) == 7}


def possible_words(letters_on_display):
    """
    This function returns every word that could be guessed,
    with the 7 letters on screen that has the middle letter,
    and isn't filtered out already
    :param: The 7 seven letters that are on display in the game
    :return: all verified words that can be made from the 7 letters on screen.
    """
    words_set = filter_list
    # all words that passed the filtering stage

    good_words = []
    for word in words_set:
        counter = 0
        for car in word:
            if car not in letters_on_display:
                break
            counter += 1
            # Checks if character is in current word, if it is not the case,
            # it will cause a break,
            # otherwise the word passes this section

            if len(word) == counter and letters_on_display[0] in word:
                good_words.append(word)
            # The word will be appended when all the letters
            # match the letters on screen and
            # if the middle letter of the hive is in the word.

    return good_words


def filter_words():
    """
    This function takes the words_list and cusswords and,
    cleans the words in the words_list,
    till they are good enough to use for words in the spelling bee.
    The outcome is every possible word,
    that could be guessed en would be right.
    :return: set with all words that fulfill
    the needs of the spelling bee rules
    """
    words, curse_words = get_files()

    exceptions = string.punctuation + string.digits + " \t\xb2\xb3\u2082\xb4"
    # This line includes punctuation, superscript,
    # subscript and digits, out of the words. (these are exceptions)

    clean_list = [word.replace('\n', "")
                  for word in words if not any(p in word for p in exceptions)]
    # Clears every element from newlines and
    # filters out words that have "an exception" in them.

    clean_list = {unidecode.unidecode(word) for word in clean_list
                  if len(word) >= 4 and not word[0] == word[0].upper()}
    # This filters out accents,
    # words with a length less than 4 letters and,
    # words where the first letter is uppercase.

    better_words = set()
    for word in clean_list:
        letters_in_word = {char for char in word}
        if len(letters_in_word) < 8:
            better_words.add(word)
        letters_in_word = {}
    # This filters out words that have more than 7 different letters in them.

    return better_words - curse_words


def get_files():
    """
    This function gets data from woorden.txt in the from of normal Dutch words
    and it gets data from scheldwoorden.txt
    in the form of Dutch swearwords(cussing).
    :return: 2 sorts of data as in,
    a list with normal words and a list with swearwords(cussing)
    """
    woorden_path = Path(__file__).parent / "woorden.txt"
    scheldwoorden_path = Path(__file__).parent / "scheldwoorden.txt"
    with open(woorden_path, 'r', encoding='utf-8') as w:
        data = w.readlines()
    with open(scheldwoorden_path, 'r', encoding='utf-8') as s:
        scheldwoorden = set(s.readlines())
    return data, scheldwoorden


filter_list = filter_words()
# This is a global variable used for storing the filtered list.
# Once someone presses new hive,
# the system will not execute the whole filter again,
# but it will just go to this variable
# where the list is already stored (saves lots of time).


def main():
    pass


if __name__ == "__main__":
    main()
