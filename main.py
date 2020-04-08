from Project.interface.interface import *
from Project.interface.Gamestate import GameState


def main():
    print("loading . . .")
    stdscr, h, w = create_screen()  # just initialize a screen, doesn't do anything
    gamestate = GameState()

    while 1:
        welcome_screen(stdscr, h, w)  # put a welcome screen on stdscr
        gamestate.reset_game()
        play_screen(stdscr, h, w)  # clear screen, put lay out for the game on stdscr
        add_word(stdscr, gamestate.letters, h, w)  # add first word to screen
        list_of_results = []

        while 1:  # play game itself
            update_words_found(stdscr, list_of_results, h, w, gamestate.score, len(gamestate.word_set))
            input_str = user_input(stdscr, h, w)  # ask user for input

            if input_str == "exit game":  # check if user wants to leave, show title screen
                title_screen(stdscr, gamestate.score, h, w, len(list_of_results))
                break

            elif input_str == "new hive":  # if the user wants a new hive
                gamestate.reset_game()
                add_word(stdscr, gamestate.letters, h, w)

            else:  # the input is a guess and it is processed
                result = gamestate.is_correct(input_str)

                if len(result) == 1:
                    give_feedback(stdscr, result[0], h, w)

                else:
                    give_feedback(stdscr, result[0], h, w)
                    list_of_results.append((input_str, result[1]))
                    update_words_found(stdscr, list_of_results, h, w, gamestate.score, len(gamestate.word_set))


if __name__ == '__main__':
    main()
