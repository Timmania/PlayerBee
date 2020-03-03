import curses as cs
import time
from curses import textpad
import signal

def welcome(screen):
    h, w = screen.getmaxyx()
    x = w // 2 - 26
    y = h // 2 - 2
    screen.addstr(y - 4, x, "  _____  _                         ____             ")
    screen.addstr(y - 3, x, " |  __ \| |                       |  _ \            ")
    screen.addstr(y - 2, x, " | |__) | | __ _ _   _  ___ _ __  | |_) | ___  ___  ")
    screen.addstr(y - 1, x, " |  ___/| |/ _` | | | |/ _ \ '__| |  _ < / _ \/ _ \ ")
    screen.addstr(y, x,     " | |    | | (_| | |_| |  __/ |    | |_) |  __/  __/ ")
    screen.addstr(y + 1, x, " |_|    |_|\__,_|\__, |\___|_|    |____/ \___|\___| ")
    screen.addstr(y + 2, x, "                  __/ |                             ")
    screen.addstr(y + 3, x, "                 |___/                              ")
    screen.addstr(y + 5, x + 13, "press enter to play a game")
    screen.refresh()
    key = screen.getch()
    if key == cs.KEY_ENTER or key in [10, 13]:
        screen.clear()
        screen.refresh()

def hiven_screen(screen, word):
    h, w = screen.getmaxyx()
    x = w // 2 - 21
    y = h // 2 - 1
    screen.addstr(y-7, x, "                _______                  ")
    screen.addstr(y-6, x, "              /         \                ")
    screen.addstr(y-5, x, "   _______   /     {0}     \   _______     ".format(word[1]))
    screen.addstr(y-4, x, " /         \ \           / /         \   ")
    screen.addstr(y-3, x, "/     {0}     \ \ _______ / /     {1}     \  ".format(word[6], word[2]))
    screen.addstr(y-2, x, "\           /   _______   \           /  ")
    screen.addstr(y-1, x, " \ _______ /  /         \  \ _______ /   ")
    screen.addstr(y, x,   "   _______   /     {0}     \   _______     ".format(word[0]))
    screen.addstr(y+1, x, " /         \ \           / /         \   ")
    screen.addstr(y+2, x, "/     {0}     \ \ _______ / /     {1}     \  ".format(word[5], word[3]))
    screen.addstr(y+3, x, "\           /   _______   \           /  ")
    screen.addstr(y+4, x, " \ _______ /  /         \  \ _______ /   ")
    screen.addstr(y+5, x, "             /     {0}     \               ".format(word[4]))
    screen.addstr(y+6, x, "             \           /               ")
    screen.addstr(y+7, x, "              \ _______ /                ")
    screen.refresh()

def input_screen(screen):
    h, w = screen.getmaxyx()
    x = w // 2 - 26
    y = h // 2
    textpad.rectangle(screen, 0, 21, 2, 50)
    screen.addstr(1, x, "enter  a word ")
    screen.refresh()

def words_found(screen):
    h, w = screen.getmaxyx()
    x = w // 2 - 18
    y = h // 2
    textpad.rectangle(screen, 0, x, 2, x + 40)
    screen.addstr(1, x + 14, "words found:")
    screen.addstr(3, x, "      words:            points: ")
    screen.refresh()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')


def main(stdscr):
    h, w = stdscr.getmaxyx()

    welcome(stdscr)

    hiven_scr = cs.newwin(h - 3, w // 2, 0, 0)
    hiven_screen(hiven_scr, ["B", "P", "L", "A", "Y", "E", "R"])

    inp_scr = cs.newwin(3, w // 2, h-4, 0)
    input_screen(inp_scr)

    words_scr = cs.newwin(h, w // 2, 0, w//2)
    words_found(words_scr)

    user_input = cs.newwin(1, 27, h-3, 23)

    cs.echo()
    cs.nocbreak()
    cs.unctrl(1)
    enu = 0
    s = ""

    while s != "exit game":
        s = user_input.getstr(0,0, 27).strip().decode("utf-8")
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

cs.wrapper(main)
