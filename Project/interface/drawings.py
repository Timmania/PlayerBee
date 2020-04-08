import curses as cs
from curses import textpad


def player_b(screen, center_y, center_x):
    """
    Writes text "Player Bee" to the screen.
    :return: nothing, just writes to the screen.
    """
    x = center_x - 26
    screen.addstr(center_y - 4, x, "  _____  _                         ____             ")
    screen.addstr(center_y - 3, x, " |  __ \| |                       |  _ \            ")
    screen.addstr(center_y - 2, x, " | |__) | | __ _ _   _  ___ _ __  | |_) | ___  ___  ")
    screen.addstr(center_y - 1, x, " |  ___/| |/ _` | | | |/ _ \ '__| |  _ < / _ \/ _ \ ")
    screen.addstr(center_y,     x, " | |    | | (_| | |_| |  __/ |    | |_) |  __/  __/ ")
    screen.addstr(center_y + 1, x, " |_|    |_|\__,_|\__, |\___|_|    |____/ \___|\___| ")
    screen.addstr(center_y + 2, x, "                  __/ |                             ")
    screen.addstr(center_y + 3, x, "                 |___/                              ")


def menu_block(screen, y, center_x, current_idx):
    """
        Writes the menu to the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 26
    menu = ["Play game", "instructions", "Game rules", "Exit game"]
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
    screen.addstr(center_y,     x, "   _______   /           \   _______    ")
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
    screen.addstr(center_y - 2, x, "Type a word:")
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 40)


def words_found_block(screen, center_y, center_x):
    """
        Creates a block on the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 24
    screen.addstr(center_y, x + 1, "{0:^47}".format("Words found"))
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 48)
    screen.addstr(center_y + 2, x + 4, "{0:<18}{1:>25}".format("Words:", "Points:"))


def game_info_block(screen, center_y, center_x):
    """
        Writes some game info on the screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 24
    textpad.rectangle(screen, center_y - 1, x, center_y + 1, x + 7)
    textpad.rectangle(screen, center_y - 1, x + 8, center_y + 1, x + 28)
    textpad.rectangle(screen, center_y - 1, x + 29, center_y + 1, x + 48)

    screen.addstr(center_y, x + 1, "{0:^6}".format("HINT"))

    screen.addstr(center_y, x + 9, "{0}".format("Total points : "))
    screen.addstr(center_y, x + 24, "{0:^4}".format("0"))

    screen.addstr(center_y, x + 31, "{0}".format("Words left : "))
    screen.addstr(center_y, x + 44, "{0:^4}".format("???"))

    screen.addstr(center_y - 3, x + 4, "{0:<44}".format("Type: 'exit game' to exit"))
    screen.addstr(center_y - 2, x + 4, "{0:<44}".format("Type: 'new hive'  to get new letters"))


def result_block(screen, center_y, center_x, tot_points):
    """
        Create the result screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 26
    screen.addstr(center_y - 3, x, " __     __                                    _ _   ")
    screen.addstr(center_y - 2, x, " \ \   / /                                   | | |  ")
    screen.addstr(center_y - 1, x, "  \ \_/ /__  _   _ _ __   _ __ ___  ___ _   _| | |_ ")
    screen.addstr(center_y, x,     "   \   / _ \| | | | '__| | '__/ _ \/ __| | | | | __|")
    screen.addstr(center_y + 1, x, "    | | (_) | |_| | |    | | |  __/\__ \ |_| | | |_ ")
    screen.addstr(center_y + 2, x, "    |_|\___/ \__,_|_|    |_|  \___||___/\__,_|_|\__|")
    screen.addstr(center_y + 4, x, "{0:^52}".format(tot_points))
    screen.addstr(center_y + 6, x, "{0:^52}".format("press Enter to go to the home screen"))
    screen.addstr(center_y + 7, x, "{0:^52}".format("press Esc to exit game"))


def instructions_block(screen, center_y, center_x):
    """
        Create the instructions screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 29
    screen.addstr(center_y - 3, x, " _____           _                   _   _                  ")
    screen.addstr(center_y - 2, x, "|_   _|         | |                 | | (_)                 ")
    screen.addstr(center_y - 1, x, "  | |  _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___  ")
    screen.addstr(center_y,     x, "  | | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __| ")
    screen.addstr(center_y + 1, x, " _| |_| | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \ ")
    screen.addstr(center_y + 2, x, "|_____|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/ ")
    screen.addstr(center_y + 5, x, "{0:^52}".format("1: Something Something Something"))
    screen.addstr(center_y + 6, x, "{0:^52}".format("2: Something Something Something"))


def rules_block(screen, center_y, center_x):
    """
        Create the rules screen.
        :return: nothing, just writes to the screen.
    """
    x = center_x - 14
    screen.addstr(center_y - 3, x, "  _____       _            ")
    screen.addstr(center_y - 2, x, " |  __ \     | |           ")
    screen.addstr(center_y - 1, x, " | |__) |   _| | ___  ___  ")
    screen.addstr(center_y,     x, " |  _  / | | | |/ _ \/ __| ")
    screen.addstr(center_y + 1, x, " | | \ \ |_| | |  __/\__ \ ")
    screen.addstr(center_y + 2, x, " |_|  \_\__,_|_|\___||___/ ")
    x -= 12
    screen.addstr(center_y + 5, x, "{0:^52}".format("1: Something Something Something"))
    screen.addstr(center_y + 6, x, "{0:^52}".format("2: Something Something Something"))