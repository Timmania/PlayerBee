#!/usr/bin/python3
""" dit programma filtert alle woorden op woorden die voldoen aan de specificaties en haalt woorden die niet voldoen ertussenuit"""

# TODO zorg ff dat je een programma maakt van de mogelijke woorden met deze letters.

import string

def remove_change_good(words):
    good_words = []
    for word in words:
        if len(word) >= 4 and word not in "0123456789" and word not in "\'\"-\xb2\xb3\u2082\xb4+.,":
            good_words.append(word)
    return good_words

def proberen(words):
    exceptions = string.punctuation + string.digits + "\t\xb2\xb3\u2082\xb4"                # punctuation, getallen, lage en hoge getallen
    clean_list = [word.replace('\n', "") for word in words if not any(p in word for p in exceptions)] #haalt hier de enters uit elk element en checkt op de exceptions
    clean_list = [word for word in clean_list if len(word) >=4]
    clean_list = [word for word in clean_list if not word[0] ==  word[0].upper()]                   #haalt hij de woorden eruit die als eerste een hoofdletter hebben
    return (clean_list)

def main():
    """
                Dit moet er gebeuren:

                De volgende woorden gaan we verwijderen:
                - woorden met meer dan 7 verschillende letters
         #       - Woorden met minder dan 4 letters
         #       - Woorden met getallen
         #       - Woorden met punctuatie
         #       - Woorden met als eerste letter een hoofdletter
         #       - Woorden met een laag of hoog getal zoals CO₂-heffing (superscript, subscript)
                - Scheldwoorden (met behulp van een andere set als die gevonden kan worden, anders gaan we een andere lijst opzoeken)

                De volgende woorden gaan we aanpassen:
                - Woorden met 1 of meerdere accenten zoals ë é (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en))
                Hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan (worden aangepast naar hetzelfde woord lowercase, dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
    """
    with open('woorden.txt', 'r') as w:
        data = w.readlines()
        good_words_set = proberen(data)
    print (good_words_set)

if __name__ == "__main__":
    main()
