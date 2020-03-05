import curses as cs
from Gamestate import GameState
from curses import textpad
import time


def welcome_screen(screen: object):
    """ Creates a welcome screen, waits until user presses Enter or Esc.
        TODO Pages like instructions/rules need to be added.
        call this function to clear screen and show welcome screen
        :param screen:
    """
    cs.noecho()
    h, w = screen.getmaxyx()
    if h < 19 or w < 80:
        print("screen is to small")
        exit(0)
    x = w // 2 - 26
    y = h // 2 - 2
    screen.clear()
    screen.addstr(y - 4, x, "  _____  _                         ____             ")
    screen.addstr(y - 3, x, " |  __ \| |                       |  _ \            ")
    screen.addstr(y - 2, x, " | |__) | | __ _ _   _  ___ _ __  | |_) | ___  ___  ")
    screen.addstr(y - 1, x, " |  ___/| |/ _` | | | |/ _ \ '__| |  _ < / _ \/ _ \ ")
    screen.addstr(y, x,     " | |    | | (_| | |_| |  __/ |    | |_) |  __/  __/ ")
    screen.addstr(y + 1, x, " |_|    |_|\__,_|\__, |\___|_|    |____/ \___|\___| ")
    screen.addstr(y + 2, x, "                  __/ |                             ")
    screen.addstr(y + 3, x, "                 |___/                              ")
    screen.addstr(y + 5, x, "{0:^52}".format("press Enter to play game"))
    screen.addstr(y + 6, x, "{0:^52}".format("press Esc to exit game"))
    screen.refresh()
    while 1:
        key = screen.getch()
        if key == 10:
            screen.clear()
            screen.refresh()
            cs.echo()
            break
        if key == 27:
            exit(0)


def play_screen(screen: object):
    """ Puts the lay-out on the screen for the game itself.
        TODO find fix for resizing screen
        :param screen:
    """
    h, w = screen.getmaxyx()

    # create hive figure
    y = (h-4)//2
    x = w//4 - 19
    screen.addstr(y - 7, x, "                _______                 ")
    screen.addstr(y - 6, x, "              /         \               ")
    screen.addstr(y - 5, x, "   _______   /           \   _______    ")
    screen.addstr(y - 4, x, " /         \ \           / /         \  ")
    screen.addstr(y - 3, x, "/           \ \ _______ / /           \ ")
    screen.addstr(y - 2, x, "\           /   _______   \           / ")
    screen.addstr(y - 1, x, " \ _______ /  /         \  \ _______ /  ")
    screen.addstr(y, x,     "   _______   /           \   _______    ")
    screen.addstr(y + 1, x, " /         \ \           / /         \  ")
    screen.addstr(y + 2, x, "/           \ \ _______ / /           \ ")
    screen.addstr(y + 3, x, "\           /   _______   \           / ")
    screen.addstr(y + 4, x, " \ _______ /  /         \  \ _______ /  ")
    screen.addstr(y + 5, x, "             /           \              ")
    screen.addstr(y + 6, x, "             \           /              ")
    screen.addstr(y + 7, x, "              \ _______ /               ")

    # create input block
    screen.addstr(h-4, x - 5, "Enter a word:")
    textpad.rectangle(screen, h - 3, x - 5, h-1, x + 43)

    # create words found block:
    y = 0
    x = (w // 4)*3 - 20
    screen.addstr(y + 1, x, "{0:^39}".format("Words found"))
    textpad.rectangle(screen, y, x, y + 2, x + 40)
    screen.addstr(y + 3, x + 3, "{0:<18}{1:>17}".format("Words:", "Points:"))

    screen.refresh()


def add_word(screen: object, word: list) -> object:
    """ Add word to the screen. this should only be done when required.
        The characters should fit nicely into the hive.
        This function does not clear anything, only overwrite.
        :param screen:
        :type word: list:
    """
    h, w = screen.getmaxyx()
    y = (h - 4) // 2
    x = w // 4
    screen.addstr(y, x, word[0])
    screen.addstr(y - 5, x, word[1])
    screen.addstr(y - 3, x + 13, word[2])
    screen.addstr(y + 2, x + 13, word[3])
    screen.addstr(y + 5, x, word[4])
    screen.addstr(y + 2, x - 13, word[5])
    screen.addstr(y - 3, x - 13, word[6])
    screen.refresh()


def user_input(screen: object) -> str:
    """ Asks the user to input a word.
        Upon hitting enter, the typed characters will be returned.
        The returned string is stripped and lower.
        :type screen: object
    """
    h, w = screen.getmaxyx()
    x = w // 4 - 17
    inp_scr = screen.subwin(1, 21, h - 2, x)
    s = inp_scr.getstr(0, 0, 20).strip().decode("utf-8").lower()
    inp_scr.clear()
    inp_scr.refresh()
    return s


def give_feedback(screen: object, feedback: str):
    """ prints out the feedback of the last given answer.
        Feedback should be a message or the points received.
        TODO look at the position of input screen and the text above
        :param screen:
        :param feedback:
    """
    h, w = screen.getmaxyx()
    x = w // 4 + 24 - len(feedback)
    screen.addstr(h - 4, x, "{0}".format(feedback))
    screen.refresh()


def title_screen(screen: object, tot_points: int):
    """ After the user typed exit game, this screen will show.
        The user can go to the home screen and play again or exit the game.
        :param screen:
        :param tot_points:
    """
    screen.clear()
    h, w = screen.getmaxyx()
    x = w // 2 - 26
    y = h // 2 - 5
    screen.addstr(y - 3, x, " __     __                                    _ _   ")
    screen.addstr(y - 2, x, " \ \   / /                                   | | |  ")
    screen.addstr(y - 1, x, "  \ \_/ /__  _   _ _ __   _ __ ___  ___ _   _| | |_ ")
    screen.addstr(y, x,     "   \   / _ \| | | | '__| | '__/ _ \/ __| | | | | __|")
    screen.addstr(y + 1, x, "    | | (_) | |_| | |    | | |  __/\__ \ |_| | | |_ ")
    screen.addstr(y + 2, x, "    |_|\___/ \__,_|_|    |_|  \___||___/\__,_|_|\__|")
    screen.addstr(y + 4, x, "{0:^52}".format(tot_points))
    screen.addstr(y + 6, x, "{0:^52}".format("press Enter to go to the home screen"))
    screen.addstr(y + 7, x, "{0:^52}".format("press Esc to exit game"))
    screen.refresh()
    while 1:
        key = screen.getch()
        if key == 10:
            screen.clear()
            screen.refresh()
            cs.echo()
            break
        if key == 27:
            exit(0)
    # show points
    # thank the player
    # made by bla bla bla
    pass


def update_words_found(screen: object, list_of_results: list):
    """ update the word_list on the right of the screen.
        The word plus the score of that word will be shown.
        Only correct guessed words are shown.
        TODO fix this function
        :param screen:
        :param list_of_results:
    """
    h, w = screen.getmaxyx()
    y = 0
    x = (w // 4) * 3 - 20
    n_terms = len(list_of_results)
    if n_terms <= 10:
        for n in range(n_terms):
            screen.addstr(y + 4 + n, x + 3, "{0:<21}{1:>14}".format(list_of_results[n][0], list_of_results[n][1]))
    elif n_terms == 11:
        screen.addstr(y + 4 + 0, x + 3, "{0:<21}{1:>14}".format("...", "."))
        for n in range(1, n_terms):
            screen.addstr(y + 4 + n, x + 3, "{0:<21}{1:>14}".format(list_of_results[n_terms-(9-n)][0], list_of_results[n_terms-(9-n)][1]))
            time.sleep(1)
    elif n_terms == 12:
        screen.addstr(y + 4 + 0, x + 3, "{0:<21}{1:>14}".format("...", "."))
        screen.addstr(y + 4 + 1, x + 3, "{0:<21}{1:>14}".format("...", "."))
        for n in range(2, n_terms):
            screen.addstr(y + 4 + n, x + 3, "{0:<21}{1:>14}".format(list_of_results[n_terms-(10-n)][0], list_of_results[n_terms-(10-n)][1]))
    else:
        screen.addstr(y + 4 + 0, x + 3, "{0:<21}{1:>14}".format("...", "."))
        screen.addstr(y + 4 + 1, x + 3, "{0:<21}{1:>14}".format("...", "."))
        screen.addstr(y + 4 + 2, x + 3, "{0:<21}{1:>14}".format("...", "."))
        for n in range(n_terms-10, n_terms):
            screen.addstr(y + 4 + n, x + 3, "{0:<21}{1:>14}".format(list_of_results[n_terms-(10-n)][0], list_of_results[n_terms-(10-n)][1]))
    screen.refresh()


def main():
    stdscr = cs.initscr()                   # just initialize a screen, doesn't do anything
    # gamestate = GameState()
    get_word = ["B", "P", "L", "A", "Y", "E", "R"]
    while 1:
        welcome_screen(stdscr)              # put a welcome screen on stdscr
        play_screen(stdscr)                 # clear screen, put lay out for the game on stdscr
        add_word(stdscr, get_word)          # add first word to screen
        list_of_results = []
        while 1:                            # play game
            input_str = user_input(stdscr)
            if input_str == "exit game":
                title_screen(stdscr, 8)     # 8 should be gamestate.get_score()
                break
            elif input_str == "new hive":
                add_word(stdscr, ["A", "G", "C", "H", "S", "E", "R"])
            else:
                result = ("Middle letter not in guess", len(input_str))
                if len(result) == 1:
                    give_feedback(stdscr, result[0])
                else:
                    give_feedback(stdscr, result[0])
                    list_of_results.append((input_str, result[1]))
                    print(list_of_results)
                    update_words_found(stdscr, list_of_results)





if __name__ == "__main__":
    main()