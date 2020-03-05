#!/usr/bin/python3
""" dit programma filtert alle woorden op woorden die voldoen aan de specificaties en haalt woorden die niet voldoen ertussenuit"""


def remove_change_good(words):
    good_words = []
    for word in words:
        if len(word) >= 4:    #minder dan 4                                                      #dit is eerst ff zodat ik kan zien welke stappen ik al heb gedaan, list comprehensions komen later
            good_words = [word for char in word if char not in "0123456789" and char not in "\'\"-\xb2\xb3\u2082\xb4+.,"]
    return good_words

# de output klopt nog niet helemaal helaas maar hier is een begin, ik ga vanavond verder, nu eerst ff m'n fiets ophalen
#    good_words = []
#    for i in range(len(words)):
#        if len(words[i]) >=4:
#            for I in range(len(words[i])):
#            if "0123456789" not in words[i] and "\'\"-\xb2\xb3\u2082\xb4+.," not in words[i]:
#                good_words.append(words[i])
#    return good_words

#class of module, de volledige of aangepast woordenset

def main():
    """
                Dit moet er gebeuren:

                De volgende woorden gaan we verwijderen:
                - woorden met meer dan 7 verschillende letters
                - Woorden met minder dan 4 letters
                - Woorden met getallen
                - Woorden met punctuatie
                - Woorden met als eerste letter een hoofdletter
                - Woorden met een laag of hoog getal zoals CO₂-heffing (superscript, subscript)
                - Scheldwoorden (met behulp van een andere set als die gevonden kan worden, anders gaan we een andere lijst opzoeken)

                De volgende woorden gaan we aanpassen:
                - Woorden met 1 of meerdere accenten zoals ë é (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en))
                Hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan (worden aangepast naar hetzelfde woord lowercase, dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
    """
    with open('woorden.txt', 'r') as w:
        data = w.readlines()
        good_words_set = remove_change_good(data)
    print (good_words_set)

if __name__ == "__main__":
    main()
