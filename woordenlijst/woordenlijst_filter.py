#!/usr/bin/python3
"""
                Dit programma filtert alle woorden op volgende de specificaties:

                De volgende woorden gaan we verwijderen:
                - woorden met meer dan 7 verschillende letters
                - Woorden met minder dan 4 letters
                - Woorden met getallen
                - Woorden met punctuatie
                - Woorden met als eerste letter een hoofdletter
                - Woorden met een laag of hoog getal zoals CO₂-heffing (superscript, subscript)
                - Scheldwoorden (met behulp van een andere set van woorden)

                De volgende woorden gaan we aanpassen:
                - Woorden met 1 of meerdere accenten zoals ë é (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en)),
                  hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan (worden aangepast naar hetzelfde woord lowercase,
                  dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
"""

# TODO zorg ff dat je een programma maakt van de mogelijke woorden met de letters die in de spelling bee komen te staan tijdens het spelen.

import string
import unidecode

def filter(words, curse_words):

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

    return (better_words - curse_words)


def main():
    with open('woorden.txt', 'r') as w:
        data = w.readlines()
    with open ('scheldwoorden.txt', 'r') as s:
        scheldwoorden = set(s.readlines())
    good_words_set = filter(data, scheldwoorden)
    print (good_words_set)

if __name__ == "__main__":
    main()
