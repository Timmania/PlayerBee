import curses as cs
from Project.interface import drawings


def create_screen():
    """ This function initializes a screen.
        It also changes some settings to work properly.
        checks if the screen is big enough to fit elements nicely.
        :return: screen
    """
    screen = cs.initscr()
    h, w = screen.getmaxyx()
    if h < 28:
        print("screen is to small, try making it bigger. \n"
              "height must be 28 lines or more. (now " + h + ") \n")
        cs.endwin()
        exit(0)
    if w < 105:
        print("screen is to small, try making it bigger. \n"
              "Width must be 105 columns or more. (now " + w + ") \n")
        cs.endwin()
        exit(0)
    cs.noecho()
    cs.curs_set(0)
    cs.cbreak()
    screen.keypad(1)
    cs.start_color()
    cs.init_pair(1, cs.COLOR_BLACK, cs.COLOR_WHITE)
    return screen, h, w


def welcome_screen(screen: object, h, w):
    """ Creates a welcome screen, waits until user presses Enter or Esc.
        call this function to clear screen and show welcome screen
        :param w:
        :param h:
        :param screen:
    """
    x = w // 2
    y = h // 2 - 4
    current_idx = 0
    while 1:
        screen.clear()
        drawings.player_b(screen, y, x)
        drawings.menu_block(screen, y + 6, x, current_idx)
        screen.refresh()

        key = screen.getch()
        if key == cs.KEY_UP and current_idx > 0:
            current_idx -= 1
        elif key == cs.KEY_DOWN and current_idx < 3:
            current_idx += 1
        if key == 10:
            screen.clear()
            if current_idx == 0:
                screen.refresh()
                break
            if current_idx == 1:
                drawings.instructions_block(screen, y, x, h, w)
                screen.refresh()
            if current_idx == 2:
                drawings.points_block(screen, y, x)
                screen.refresh()
                screen.getch()
            if current_idx == 3:
                screen.clear()
                screen.refresh()
                cs.echo()
                cs.curs_set(1)
                screen.keypad(False)
                cs.nocbreak()
                cs.endwin()
                exit(0)
        if key == 27:
            cs.echo()
            cs.curs_set(1)
            screen.keypad(False)
            cs.nocbreak()
            cs.endwin()
            exit(0)

        drawings.menu_block(screen, y + 6, x, current_idx)


def play_screen(screen: object, h, w):
    """ Puts the lay-out on the screen for the game itself.
        TODO find fix for resizing screen
        :param w:
        :param h:
        :param screen:
    """
    # create hive figure
    y = (h - 6) // 2
    x = w // 4
    drawings.hiven(screen, y, x)
    drawings.input_block(screen, h - 2, x)  # create input block

    x = (w // 4) * 3
    drawings.words_found_block(screen, 2, x, 0)  # create words found block:
    drawings.game_info_block(screen, h - 2, x)
    screen.refresh()


def difficulty_block(screen: object, h, w, difficulty):
    x = w // 4
    drawings.difficulty_block(screen, 2, x, difficulty)


def update_words_found_int(screen: object, h, w, words_found):
    x = (w // 4) * 3
    drawings.words_found_block(screen, 2, x, words_found)


def add_word(screen: object, word: list, h, w):
    """ Add word to the screen. this should only be done when required.
        The characters should fit nicely into the hive.
        This function does not clear anything, only overwrite.
        :param w:
        :param h:
        :param screen:
        :type word: list:
    """
    y = (h - 6) // 2
    x = w // 4
    screen.addstr(y, x, word[0])
    screen.addstr(y - 5, x, word[1])
    screen.addstr(y - 3, x + 13, word[2])
    screen.addstr(y + 2, x + 13, word[3])
    screen.addstr(y + 5, x, word[4])
    screen.addstr(y + 2, x - 13, word[5])
    screen.addstr(y - 3, x - 13, word[6])
    screen.refresh()


def user_input(screen: object, h, w) -> str:
    """ Asks the user to input a word.
        Upon hitting enter, the typed characters will be returned.
        The returned string is stripped and lower.
        :param w:
        :param h:
        :type screen: object
    """
    x = w // 4 - 22
    inp_scr = screen.subwin(1, 21, h - 2, x)
    cs.curs_set(1)
    cs.echo()
    s = inp_scr.getstr(0, 0, 20).strip().decode("utf-8").lower()
    cs.noecho()
    cs.curs_set(0)
    inp_scr.clear()
    inp_scr.refresh()
    return s


def give_feedback(screen: object, feedback: str, h, w):
    """ prints out the feedback of the last given answer.
        Feedback should be a message or the points received.
        TODO look at the position of input screen and the text above
        :param w:
        :param h:
        :param screen:
        :param feedback:
    """
    x = w // 4 - 10
    screen.addstr(h - 4, x, "{0:>34}".format(feedback))
    screen.refresh()


def give_hint(screen, hint, h, w):
    x = w // 4 - 17
    screen.addstr(h - 2, x, "{0}".format(hint))
    screen.refresh()


def title_screen(screen: object, tot_points: int, h, w, words_guested):
    """ After the user typed exit game, this screen will show.
        The user can go to the home screen or exit the game.
        :param w:
        :param h:
        :param screen:
        :param tot_points:
    """
    screen.clear()
    x = w // 2
    y = h // 2 - 5
    drawings.result_block(screen, y, x, tot_points, words_guested)
    screen.refresh()
    while 1:
        key = screen.getch()
        if key == 10:
            screen.clear()
            screen.refresh()
            break
        if key == 27:
            cs.echo()
            cs.curs_set(1)
            screen.keypad(False)
            cs.nocbreak()
            cs.endwin()
            exit(0)


def update_words_found(screen: object, list_of_results: list, h, w, tot_points, len_set):
    """ update the word_list on the right of the screen.
        The word plus the score of that word will be shown.
        Only correct guessed words are shown.
        TODO fix this function
        :param w:
        :param h:
        :param screen:
        :param list_of_results:
    """
    y = 5
    x = (w // 4) * 3 - 18
    n_words = len(list_of_results)
    n_lines = (h - 10) // 4 * 3
    if n_words <= n_lines:
        for n in range(0, n_words):
            screen.addstr(y + n, x, "{0:<20}{1:>17}".format(list_of_results[n][0],
                                                            list_of_results[n][1]))
    elif n_words == n_lines:
        screen.addstr(y, x, "{0:<19}{1:>18}".format("...", "..."))
        for n in range(1, n_lines):
            screen.addstr(y + n, x, "{0:<20}{1:>17}".format(list_of_results[n][0],
                                                            list_of_results[n][1]))
    else:
        screen.addstr(y, x, "{0:<19}{1:>18}".format("...", "..."))
        p = n_words - n_lines
        for n in range(1, n_lines):
            screen.addstr(y + n, x, "{0:<20}{1:>17}".format(list_of_results[p + n][0],
                                                            list_of_results[p + n][1]))
    screen.addstr(h - 2, x + 12, "{0:^4}".format(tot_points))
    screen.addstr(h - 2, x + 38, "{0:^4}".format(len_set))
    screen.refresh()


def main():
    pass


if __name__ == "__main__":
    main()
