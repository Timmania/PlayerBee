import curses as cs
from curses import textpad


class Screens:
    """ Initialize the standard screen of the game.
        Everything will be put on this screen.
        Create an object to create screen.
        """
    def __init__(self):
        self.stdscr = cs.initscr()
        self.h, self.w = self.stdscr.getmaxyx()


    def welcome_screen(self):
        """ Creates a welcome screen, waits until user presses Enter.
            TODO Pages like instructions/rules need to be added.
            After object is created, call this method to show welcome screen.
        """
        x = self.w // 2 - 26
        y = self.h // 2 - 2
        self.stdscr.addstr(y - 4, x, "  _____  _                         ____             ")
        self.stdscr.addstr(y - 3, x, " |  __ \| |                       |  _ \            ")
        self.stdscr.addstr(y - 2, x, " | |__) | | __ _ _   _  ___ _ __  | |_) | ___  ___  ")
        self.stdscr.addstr(y - 1, x, " |  ___/| |/ _` | | | |/ _ \ '__| |  _ < / _ \/ _ \ ")
        self.stdscr.addstr(y, x,     " | |    | | (_| | |_| |  __/ |    | |_) |  __/  __/ ")
        self.stdscr.addstr(y + 1, x, " |_|    |_|\__,_|\__, |\___|_|    |____/ \___|\___| ")
        self.stdscr.addstr(y + 2, x, "                  __/ |                             ")
        self.stdscr.addstr(y + 3, x, "                 |___/                              ")
        self.stdscr.addstr(y + 5, x + 13, "press Enter to play game")
        self.stdscr.addstr(y + 6, x + 13, "press Esc to play exit game")
        self.stdscr.refresh()

        while 1:
            key = self.stdscr.getch()
            if key == 10:
                self.stdscr.clear()
                self.stdscr.refresh()
                break
            if key == 27:
                exit(0)


    def play_screen(self, start_word):
        """ this creates a new window where the game is played.
            other objects draw things on this screen.
        """
        self.play_scr = cs.newwin(self.h, self.w, 0, 0)

        self.hiven_screen(self.)
        self.inp_screen(self.words_scr)

        self.hiven_scr = cs.newwin(self.h - 3, self.w // 2, 0, 0)
        self.hiven_screen(self.hiven_scr, start_word)

        self.inp_scr = cs.newwin(3, self.w // 2, self.h - 4, 0)
        self.input_screen(self.inp_scr)

        self.words_scr = cs.newwin(self.h, self.w // 2, 0, self.w // 2)
        self.words_found(self.words_scr)

    def hiven_screen(self, screen):
        start_word =
        h, w = screen.getmaxyx()
        x = w // 2 - 21
        y = h // 2 - 1
        screen.addstr(y - 7, x, "                _______                  ")
        screen.addstr(y - 6, x, "              /         \                ")
        screen.addstr(y - 5, x, "   _______   /     {0}     \   _______     ".format(start_word[1]))
        screen.addstr(y - 4, x, " /         \ \           / /         \   ")
        screen.addstr(y - 3, x, "/     {0}     \ \ _______ / /     {1}     \  ".format(start_word[6], start_word[2]))
        screen.addstr(y - 2, x, "\           /   _______   \           /  ")
        screen.addstr(y - 1, x, " \ _______ /  /         \  \ _______ /   ")
        screen.addstr(y, x, "   _______   /     {0}     \   _______     ".format(start_word[0]))
        screen.addstr(y + 1, x, " /         \ \           / /         \   ")
        screen.addstr(y + 2, x, "/     {0}     \ \ _______ / /     {1}     \  ".format(start_word[5], start_word[3]))
        screen.addstr(y + 3, x, "\           /   _______   \           /  ")
        screen.addstr(y + 4, x, " \ _______ /  /         \  \ _______ /   ")
        screen.addstr(y + 5, x, "             /     {0}     \               ".format(start_word[4]))
        screen.addstr(y + 6, x, "             \           /               ")
        screen.addstr(y + 7, x, "              \ _______ /                ")
        screen.refresh()

    def input_screen(self, screen):
        h, w = screen.getmaxyx()
        x = w // 2 - 26
        y = h // 2
        textpad.rectangle(screen, 0, 21, 2, 50)
        screen.addstr(1, x, "enter  a word ")
        screen.refresh()

    def words_found(self, screen):
        h, w = screen.getmaxyx()
        x = w // 2 - 18
        y = h // 2
        textpad.rectangle(screen, 0, x, 2, x + 40)
        screen.addstr(1, x + 14, "words found:")
        screen.addstr(3, x, "      words:            points: ")
        screen.refresh()


    def play_game(self):
        cs.echo()
        self.user_input = cs.newwin(1, 27, self.h - 3, 23)
        enu = 0
        s = ""
        while s != "exit game":
            s = self.user_input.getstr(0, 0, 27).strip().decode("utf-8")
            if s == "exit game":
                self.hiven_scr.clear()
                self.hiven_scr.refresh()
                self.inp_scr.clear()
                self.inp_scr.refresh()
                self.words_scr.clear()
                self.words_scr.refresh()
                break
            self.words_scr.addstr(4 + enu, 17, s)
            self.words_scr.refresh()
            enu += 1
            if enu > 10:
                self.hiven_scr.clear()
                self.hiven_scr.refresh()
                self.inp_scr.clear()
                self.inp_scr.refresh()
                self.words_scr.clear()
                self.words_scr.refresh()
                break
            self.user_input.clear()
            self.user_input.refresh()


def main():
    window = screens()
    while 1:
        window.welcome_screen()
        window.play_screen(["B", "P", "L", "A", "Y", "E", "R"])
        window.play_game()

    exit(0)


    enu = 0
    s = ""

    while s != "exit game":
        s = user_input.getstr(0, 0, 27).strip().decode("utf-8")
        if s == "exit game":
            break
        words_scr.addstr(4 + enu, 17, s)
        words_scr.refresh()
        enu += 1
        if enu > 10:
            break
        user_input.clear()
        user_input.refresh()

    stdscr.getch()

if __name__ == "__main__":
    main()