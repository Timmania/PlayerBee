from Project.interface.interface import *
from Project.interface.Gamestate import GameState
import curses as cs


def main():
    stdscr, h, w = create_screen()  # just initialize a screen, doesn't do anything
    gamestate = GameState()
    while 1:
        welcome_screen(stdscr, h, w)  # put a welcome screen on stdscr
        gamestate.reset_game()
        play_screen(stdscr, h, w)  # clear screen, put lay out for the game on stdscr
        difficulty_block(stdscr, h, w, len(gamestate.word_set))
        add_word(stdscr, gamestate.letters, h, w)  # add first word to screen
        list_of_results = []
        results_corr = 0
        print(gamestate.word_set)

        while 1:  # play game itself
            update_words_found(stdscr, list_of_results, h, w, gamestate.score, len(gamestate.word_set))
            input_str = user_input(stdscr, h, w)  # ask user for input

            if input_str == "exit game":  # check if user wants to leave, show title screen
                title_screen(stdscr, gamestate.score, h, w, len(list_of_results))
                break

            elif input_str == "new hive":  # if the user wants a new hive
                gamestate.reset_game()
                add_word(stdscr, gamestate.letters, h, w)
                difficulty_block(stdscr, h, w, len(gamestate.word_set))
                give_feedback(stdscr, "", h, w)

            elif input_str == "give hint":
                hint = "Hint '{0}{1}'".format(gamestate.get_hint()[0], "." * gamestate.get_hint()[1])
                give_feedback(stdscr, hint, h, w)

            else:  # the input is a guess and it is processed
                result = gamestate.is_correct(input_str)

                if len(result) == 1:
                    give_feedback(stdscr, result[0], h, w)

                else:
                    list_of_results.append((input_str, result[1]))
                    if len(gamestate.word_set) == 0:
                        gamestate.reset_game()
                        add_word(stdscr, gamestate.letters, h, w)
                        difficulty_block(stdscr, h, w, len(gamestate.word_set))
                        list_of_results.append(("All words found!", 20))
                        give_feedback(stdscr, "You found all words! Congrats! +20", h, w)
                        # gamestate.score + 20 doesnt work todo gamestate.score + 20
                        results_corr += 1
                    else:
                        give_feedback(stdscr, result[0], h, w)
                    update_words_found(stdscr, list_of_results, h, w, gamestate.score, len(gamestate.word_set))
                    update_words_found_int(stdscr, h, w, len(list_of_results) - results_corr)
    cs.echo()
    cs.curs_set(1)
    stdscr.keypad(False)
    cs.nocbreak()
    cs.endwin()


if __name__ == '__main__':
    main()
