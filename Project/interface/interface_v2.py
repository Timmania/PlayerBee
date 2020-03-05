import curses as cs
from Gamestate import GameState
from curses import textpad


def welcome_screen(screen: object) -> object:
    """ Creates a welcome screen, waits until user presses Enter.
        TODO Pages like instructions/rules need to be added.
        After object is created, call this method to show welcome screen.
    """
    screen.addstr(0, 0, "String")


def play_screen(screen: object) -> object:
    screen.addstr(0, 0, "String")


def add_word(stdscr, word):
    pass


def user_input(stdscr):
    s = "input"
    # s will always be lower
    return s


def give_feedback(stdscr, feedback):
    pass


def title_screen(stdscr, tot_points):
    # show points
    # thank the player
    # made by bla bla bla
    pass


def update_words_found(stdscr, word, points):
    pass


def main():
    stdscr = cs.initscr()   # just initialize a screen, doesn't do anything
    while 1:
        welcome_screen(stdscr)  # put a welcome screen on stdscr
        play_screen(stdscr)     # clear screen, put lay out for the game on stdscr
        add_word(stdscr, ["B", "P", "L", "A", "Y", "E", "R"])
        while 1:                # play game
            input_str = user_input(stdscr)
            if input_str == "exit game":
                title_screen(stdscr, points)
                break
            elif input_str == "new hive":
                add_word(stdscr, ["B", "P", "L", "A", "Y", "E", "R"])
            else:
                result = GameState.is_correct(input_str)
                if len(result) == 1:
                    give_feedback(stdscr, result[0])
                else:
                    give_feedback(stdscr, result[0])
                    update_words_found(stdscr, input_str, result[1])




if __name__ == "__main__":
    main()