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
                - Woorden met 1 of meerdere accenten zoals ë é
                  (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en)),
                  hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan
                  (worden aangepast naar hetzelfde woord lowercase,
                  dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
"""
import string
import unidecode


def pangrams():
    words = filter_list
    return {word for word in words if len(word) == 7 and len(set(word)) == 7}


def pangrams_only(letters_on_display):
    words_possible = possible_words(letters_on_display)
    letters_on_display = list(letters_on_display)
    almost_pangrams = []
    for word in words_possible:
        counter = 0
        for letter in letters_on_display:
            if letter not in word:
                break
            else:
                counter = counter + 1
                if counter == len(letters_on_display):
                    if len(word) == 7:  # deze regel is alleen nodig als je perfecte super pangrams wil
                        almost_pangrams.append(word)
    return set(almost_pangrams)


def possible_words(letters_on_display):
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

            if len(word) == counter:
                good_words.append(word)
        # zijn alle chars geweest, dus heeft het algo bevestigd dat alle chars in de letters_on_display zaten dan
        # voegt hij hem hier toe

    return good_words


def filter():
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
    with open('woordenlijst/woorden.txt', 'r', encoding='utf-8') as w:
        data = w.readlines()
    with open('woordenlijst/scheldwoorden.txt', 'r', encoding='utf-8') as s:
        scheldwoorden = set(s.readlines())
    return data, scheldwoorden


filter_list = filter()


def main():
    pass


if __name__ == "__main__":
    main()
