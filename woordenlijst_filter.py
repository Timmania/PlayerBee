#!/usr/bin/python3
""" dit programma filtert alle woorden op woorden die voldoen aan de specificaties en haalt woorden die niet voldoen ertussenuit"""

def main():
    """
                Dit moet er gebeuren:

                De volgende woorden gaan we verwijderen:
                - Woorden met minder dan 4 letters
                - Woorden met getallen
                - Woorden met als eerste letter een hoofdletter
                - Woorden met een laag of hoog getal zoals CO₂-heffing
                - Scheldwoorden (met behulp van een andere set als die gevonden kan worden, anders gaan we een andere lijst opzoeken)

                De volgende woorden gaan we aanpassen:
                - Woorden met 1 of meerdere accenten zoals ë é (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en))
                Hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan (worden aangepast naar hetzelfde woord lowercase, dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
    """
    with open('woorden.txt', 'r') as w:
        data = w.readlines()
    print(data)

if __name__ == "__main__":
    main()