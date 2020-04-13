import curses as cs
from curses import textpad
from Project.interface import interface


def player_b(screen, center_y, center_x):
    """
    Writes text "Player Bee" to the screen.
    :return: nothing, just writes to the screen.
    """
    x = center_x - 26
    screen.addstr(center_y - 4, x,
                  "  _____  _                         ____             ")
    screen.addstr(center_y - 3, x,
                  " |  __ \| |                       |  _ \            ")
    screen.addstr(center_y - 2, x,
                  " | |__) | | __ _ _   _  ___ _ __  | |_) | ___  ___  ")
    screen.addstr(center_y - 1, x,
                  " |  ___/| |/ _` | | | |/ _ \ '__| |  _ < / _ \/ _ \ ")
    screen.addstr(center_y, x,
                  " | |    | | (_| | |_| |  __/ |    | |_) |  __/  __/ ")
    screen.addstr(center_y + 1, x,
                  " |_|    |_|\__,_|\__, |\___|_|    |____/ \___|\___| ")
    screen.addstr(center_y + 2, x,
                  "                  __/ |                             ")
    screen.addstr(center_y + 3, x,
                  "                 |___/                              ")


def menu_block(screen, y, center_x, current_idx):
    """
        Writes the menu to the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 26
    menu = ["Speel spel", "Instructies", "Punten systeem", "Spel verlaten"]
    for idx, row in enumerate(menu):
        if idx == current_idx:
            screen.attron(cs.color_pair(1))
            screen.addstr(y + idx, x, "{0:^52}".format(row))
            screen.attroff(cs.color_pair(1))
        else:
            screen.addstr(y + idx, x, "{0:^52}".format(row))


def hiven(screen, center_y, center_x):
    """
        Writes the hiven figure to the screen
        :return: nothing, just writes to the screen.
    """
    x = center_x - 19
    screen.addstr(center_y - 7, x, "                _______                 ")
    screen.addstr(center_y - 6, x, "              /         \               ")
    screen.addstr(center_y - 5, x, "   _______   /           \   _______    ")
    screen.addstr(center_y - 4, x, " /         \ \           / /         \  ")
    screen.addstr(center_y - 3, x, "/           \ \ _______ / /           \ ")
    screen.addstr(center_y - 2, x, "\           /   _______   \           / ")
    screen.addstr(center_y - 1, x, " \ _______ /  /         \  \ _______ /  ")
    screen.addstr(center_y, x, "   _______   /           \   _______    ")
    screen.addstr(center_y + 1, x, " /         \ \           / /         \  ")
    screen.addstr(center_y + 2, x, "/           \ \ _______ / /           \ ")
    screen.addstr(center_y + 3, x, "\           /   _______   \           / ")
    screen.addstr(center_y + 4, x, " \ _______ /  /         \  \ _______ /  ")
    screen.addstr(center_y + 5, x, "             /           \              ")
    screen.addstr(center_y + 6, x, "             \           /              ")
    screen.addstr(center_y + 7, x, "              \ _______ /               ")


def input_block(screen, center_y, center_x):
    """
        Creates a block on the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 24
    screen.addstr(center_y - 2, x, "Type een woord:")
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 48)


def words_found_block(screen, center_y, center_x, words_found):
    """
        Creates a block on the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 24
    screen.addstr(center_y, x + 1,
                  "{0:^47}".format("Woorden gevonden : " +
                                   "{0:^4}".format(str(words_found))))
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 48)
    screen.addstr(center_y + 2, x + 4,
                  "{0:<17}{1:>25}".format("Woorden:", "Punten:"))


def game_info_block(screen, center_y, center_x):
    """
        Writes some game info on the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 24
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 23)
    textpad.rectangle(screen, center_y - 1, x + 24, center_y + 1, x + 48)

    screen.addstr(center_y, x + 1, "{0:^18}".format("Totaal punten : "))
    screen.addstr(center_y, x + 19, "{0:^4}".format("0"))

    screen.addstr(center_y, x + 26, "{0:^18}".format("Woorden over : "))
    screen.addstr(center_y, x + 44, "{0:^4}".format("???"))

    screen.addstr(center_y - 4, x,
                  "{0:^48}".format("De volgende opties kun je typen :"))
    screen.addstr(center_y - 2, x,
                  " {0:^12}  |  {1:^15} | {2:^13}".format("verlaat spel",
                                                          "nieuwe letters",
                                                          "geef hint"))


def get_difficulty(difficulty):
    if difficulty <= 20:
        return "Player Bee(st)"
    elif difficulty <= 50:
        return "Moeilijk"
    elif difficulty <= 100:
        return "Medium"
    else:
        return "Easy Beesy"


def difficulty_block(screen, center_y, center_x, difficulty):
    x = center_x - 24
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 15)
    textpad.rectangle(screen, center_y - 1, x + 16, center_y + 1, x + 48)

    screen.addstr(center_y, x + 2, "{0:^13}".format("Player Bee"))
    screen.addstr(center_y, x + 18, "Moeilijkheid : ")
    screen.addstr(center_y, x + 33,
                  "{0:^14}".format(get_difficulty(difficulty)))


def result_block(screen, center_y, center_x, tot_points, words_guested):
    """
        Create the result screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 37
    screen.addstr(center_y - 3, x,
                  "       _                        _____                 _ _              _   ")
    screen.addstr(center_y - 2, x,
                  "      | |                      |  __ \               | | |            | |  ")
    screen.addstr(center_y - 1, x,
                  "      | | ___  _   ___      __ | |__) |___  ___ _   _| | |_ __ _  __ _| |_ ")
    screen.addstr(center_y, x,
                  "  _   | |/ _ \| | | \ \ /\ / / |  _  // _ \/ __| | | | | __/ _` |/ _` | __|")
    screen.addstr(center_y + 1, x,
                  " | |__| | (_) | |_| |\ V  V /  | | \ \  __/\__ \ |_| | | || (_| | (_| | |_ ")
    screen.addstr(center_y + 2, x,
                  "  \____/ \___/ \__,_| \_/\_/   |_|  \_\___||___/\__,_|_|\__\__,_|\__,_|\__|")

    screen.addstr(center_y + 5, x, "{0:^75}".format(
        "Jouw totale score was " + str(tot_points) + "!"))
    if words_guested == 1:
        screen.addstr(center_y + 6, x, "{0:^75}".format(
            "Jij raadde " + str(words_guested) + " woord"))
    else:
        screen.addstr(center_y + 6, x, "{0:^75}".format(
            "Jij raadde " + str(words_guested) + " woorden"))

    screen.addstr(center_y + 9, x, "{0:^75}".format(
        "druk op Enter om naar het startscherm te gaan."))
    screen.addstr(center_y + 10, x,
                  "{0:^75}".format("druk op Esc op het spel te verlaten."))


def instructions_block(screen, center_y, center_x, h, w):
    """
        Create the instructions screens.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 29
    screen.addstr(center_y - 3, x,
                  "  _____           _                   _   _             ")
    screen.addstr(center_y - 2, x,
                  " |_   _|         | |                 | | (_)            ")
    screen.addstr(center_y - 1, x,
                  "   | |  _ __  ___| |_ _ __ _   _  ___| |_ _  ___  ___   ")
    screen.addstr(center_y, x,
                  "   | | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \/ __|  ")
    screen.addstr(center_y + 1, x,
                  "  _| |_| | | \__ \ |_| |  | |_| | (__| |_| |  __/\__ \  ")
    screen.addstr(center_y + 2, x,
                  " |_____|_| |_|___/\__|_|   \__,_|\___|\__|_|\___||___/  ")

    screen.addstr(center_y + 5, x - 2, "{0:<52}".format(
        "Het doel van dit spel is om zoveel mogelijk punten "
        "te verdienen."))
    screen.addstr(center_y + 6, x - 2,
                  "{0:<52}".format("Dit kan gedaan worden door zoveel "
                                   "mogelijk woorden te vinden."))
    screen.addstr(center_y + 7, x - 2, "{0:<52}".format(" Op voorwaarde dat:"))
    screen.addstr(center_y + 8, x - 2,
                  "{0:<52}".format(" - Het woord is minimaal 4 letters lang."))
    screen.addstr(center_y + 9, x - 2, "{0:<52}".format(
        " - De middelste letter moet er sowieso in zitten."))
    screen.addstr(center_y + 10, x - 2,
                  "{0:<52}".format(" - Scheldwoorden leveren geen punten op."))
    screen.addstr(center_y + 11, x - 2, "{0:<52}".format(
        " - Dezelfde letter mag meerdere keren gebruikt worden."))
    screen.addstr(center_y + 13, x, "{0:^62}".format(
        "Druk op een toets voor een uitleg van het speelscherm."))
    screen.addstr(center_y + 14, x,
                  "{0:^62}".format("Druk op Esc om de uitleg te verlaten."))
    key = screen.getch()
    if key == 27:
        return ""
    y = (h - 6) // 2
    x = w // 4
    screen.clear()
    hiven(screen, y, x)
    input_block(screen, h - 2, x)  # create input block
    interface.add_word(screen, ['p', 'a', 'n', 'g', 'r', 'a', 'm'], h, w)
    difficulty_block(screen, 2, x, 100)

    x = (w // 4) * 3
    words_found_block(screen, 2, x, 1)  # create words found block:
    game_info_block(screen, h - 2, x)
    interface.update_words_found(screen, [['pangram', 14]], h, w, 14, 83)
    interface.give_feedback(screen, "PANGRAM FOUND! +14", h, w)
    instructions = [
        ["Dit is het speelscherm."],
        ["hier vind je de moeilijkheisgraat", "van de huidige letters.", 5,
         (w // 4) + 24, "nw"],
        ["Hier vind je de letters", "waarmee jij woorden moet raden.",
         (h - 6) // 2 + 6, (w // 4) + 15, "nw"],
        ["Hier kun je tijdens het spel woorden typen.", h - 10, (w // 4) - 15,
         "se"],
        ["Hier komt de feedback van jouw antwoord.", h - 11, (w // 4) + 8,
         "se"],
        ["Hier staan jouw totale punten", "en de woorden die nog over zijn.",
         h - 9, (w // 4) * 3 - 32, "se"],
        ["Hier staan opties die jij kan typen", "tijdens het spel.", h - 12,
         (w // 4) * 3 - 29, "se"],
        ["Hier staan woorden die jij al gevonden hebt.", 6, (w // 4) * 3 - 32,
         "ne"]
    ]
    current_idx = 0
    while 1:
        textpad.rectangle(screen, y - 3, x - 24, y + 6, x + 24)
        screen.addstr(y - 2, x - 7,
                      "{0} {1}/{2}".format("Instructies", current_idx + 1,
                                           len(instructions)))
        screen.addstr(y, x - 22, "{0:44}".format(instructions[current_idx][0]))
        screen.addstr(y + 1, x - 22, "{0:44}".format(""))
        if len(instructions[current_idx]) > 4:
            screen.addstr(y + 1, x - 22,
                          "{0:44}".format(instructions[current_idx][1]))
        screen.addstr(y + 3, x - 21, "{0:^44}".format(
            "Navigeer met de pijltoetsen door de uitleg."))
        screen.addstr(y + 4, x - 23, "{0:^41}".format(
            "Druk op Esc om de uitleg te verlaten."))
        if current_idx > 0:
            interface.give_feedback(screen, "PANGRAM FOUND! +14", h, w)
            arrow_screen = arrow(
                screen,
                instructions[current_idx][-3],
                instructions[current_idx][-2],
                instructions[current_idx][-1])
        screen.refresh()
        key = screen.getch()
        if current_idx > 0:
            arrow_screen.clear()
            arrow_screen.refresh()
        if (key == cs.KEY_UP or key == cs.KEY_RIGHT) and current_idx < len(
                instructions) - 1:
            current_idx += 1
        elif (key == cs.KEY_DOWN or key == cs.KEY_LEFT) and current_idx > 0:
            current_idx -= 1
        if key == 27:
            return ""


def arrow(screen, center_y, center_x, direction):
    arrow_screen = screen.subwin(6, 8, center_y, center_x)
    if direction == "nw":
        arrow_screen.addstr(0, 0, "{0}".format(" _____"))
        arrow_screen.addstr(1, 0, "{0}".format("| \\"))
        arrow_screen.addstr(2, 0, "{0}".format("|\\ \\"))
        arrow_screen.addstr(3, 0, "{0}".format("| \\ \\"))
        arrow_screen.addstr(4, 0, "{0}".format("   \\ \\"))
        arrow_screen.addstr(5, 0, "{0}".format("    \\ \\"))
    if direction == "se":
        arrow_screen.addstr(0, 0, "{0}".format("\\ \\"))
        arrow_screen.addstr(1, 0, "{0}".format(" \\ \\"))
        arrow_screen.addstr(2, 0, "{0}".format("  \\ \\  |"))
        arrow_screen.addstr(3, 0, "{0}".format("   \\ \\ |"))
        arrow_screen.addstr(4, 0, "{0}".format("    \\  |"))
        arrow_screen.addstr(5, 0, "{0}".format("  -----"))
    if direction == "ne":
        arrow_screen.addstr(0, 0, "{0}".format(" _____ "))
        arrow_screen.addstr(1, 0, "{0}".format("    / |"))
        arrow_screen.addstr(2, 0, "{0}".format("   / /|"))
        arrow_screen.addstr(3, 0, "{0}".format("  / / |"))
        arrow_screen.addstr(4, 0, "{0}".format(" / /"))
        arrow_screen.addstr(5, 0, "{0}".format("/ / "))

    arrow_screen.refresh()
    return arrow_screen


def points_block(screen, center_y, center_x):
    """
        Create the points screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 36
    screen.addstr(center_y - 3, x,
                  "  _____             _                             _                      ")
    screen.addstr(center_y - 2, x,
                  " |  __ \           | |                           | |                     ")
    screen.addstr(center_y - 1, x,
                  " | |__) |   _ _ __ | |_ ___ _ __    ___ _   _ ___| |_ ___  ___ _ __ ___  ")
    screen.addstr(center_y, x,
                  " |  ___/ | | | '_ \| __/ _ \ '_ \  / __| | | / __| __/ _ \/ _ \ '_ ` _ \ ")
    screen.addstr(center_y + 1, x,
                  " | |   | |_| | | | | ||  __/ | | | \__ \ |_| \__ \ha ||  __/  __/ | | | | |")
    screen.addstr(center_y + 2, x,
                  " |_|    \__,_|_| |_|\__\___|_| |_| |___/\__, |___/\__\___|\___|_| |_| |_|")
    screen.addstr(center_y + 3, x,
                  "                                         __/ |                           ")
    screen.addstr(center_y + 3, x,
                  "                                        |___/                            ")

    x += 5
    screen.addstr(center_y + 5, x,
                  "{0:<47}{1:<14}".format("Antwoord : ", "Aantal punten : "))
    screen.addstr(center_y + 7, x,
                  "  {0:<47}{1:<14}".format("4 letter woord", "1 punt"))
    screen.addstr(center_y + 8, x,
                  "  {0:<47}{1:<14}".format("Woorden vanaf 5 letters ",
                                            "1 punt per letter"))
    screen.addstr(center_y + 9, x, "  {0:<47}{1:<14}".format(
        "Elke letter minimaal 1 keer gebruiken", "7 extra punten"))
    screen.addstr(center_y + 10, x, "  {0:<47}{1:<14}".format(
        "Alle woorden met de gegeven letters raden",
        "20 extra punten"))
    screen.addstr(center_y + 12, x, "{0:^64}".format(
        "Druk op een toets om het punten systeem te verlaten."))
