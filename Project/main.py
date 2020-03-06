from interface.interface import *

def main():
    stdscr, h, w = create_screen()  # just initialize a screen, doesn't do anything
    # gamestate = GameState()

    while 1:
        welcome_screen(stdscr, h, w)  # put a welcome screen on stdscr
        play_screen(stdscr, h, w)  # clear screen, put lay out for the game on stdscr
        get_word = ["B", "P", "L", "A", "Y", "E", "R"]
        add_word(stdscr, get_word, h, w)  # add first word to screen
        list_of_results = []

        while 1:  # play game itself
            input_str = user_input(stdscr, h, w)  # ask user for input

            if input_str == "exit game":  # check if user wants to leave, show title screen
                title_screen(stdscr, 8, h, w)  # TODO 8 should be gamestate.get_score()
                break

            elif input_str == "new hive":  # if the user wants a new hive
                add_word(stdscr, ["A", "G", "C", "H", "S", "E", "R"], h, w)

            else:  # the input is a guess and it is processed
                result = ("Middle letter not in guess", len(input_str))  # TODO result = gamestate.is_correct()

                if len(result) == 1:
                    give_feedback(stdscr, result[0], h, w)

                else:
                    give_feedback(stdscr, result[0], h, w)
                    list_of_results.append((input_str, result[1]))
                    update_words_found(stdscr, list_of_results, h, w)


if __name__ == '__main__':
    main()
