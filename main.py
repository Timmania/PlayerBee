from Project.interface.interface import *
from Project.interface.Gamestate import GameState
import curses as cs


def main():
    stdscr, h, w = create_screen()  # just initialize a screen
    gamestate = GameState()
    while 1:
        welcome_screen(stdscr, h, w)  # put a welcome screen on stdscr
        gamestate.reset_game()
        play_screen(stdscr, h, w)  # clear screen, print lay out for the game
        difficulty_block(stdscr, w, len(gamestate.word_set))
        add_word(stdscr, gamestate.letters, h, w)  # add first word to screen
        list_of_results = []
        results_corr = 0

        while 1:  # play game itself
            update_words_found(stdscr, list_of_results, h, w,
                               gamestate.score, len(gamestate.word_set))
            input_str = user_input(stdscr, h, w)  # ask user for input

            if input_str == "verlaat spel":
                title_screen(stdscr, gamestate.score, h, w,
                             len(list_of_results) - results_corr)
                break

            elif input_str == "nieuwe letters":  # if the user wants a new hive
                gamestate.reset_game()
                add_word(stdscr, gamestate.letters, h, w)
                difficulty_block(stdscr, w, len(gamestate.word_set))
                give_feedback(stdscr, "", h, w)

            elif input_str == "geef hint":
                hint = "Hint '{0}{1}'".format(gamestate.get_hint()[0],
                                              "." * gamestate.get_hint()[1])
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
                        give_feedback(stdscr,
                                      gamestate.increase_score("all_found"), h,
                                      w)

                        results_corr += 1
                    else:
                        give_feedback(stdscr, result[0], h, w)
                    update_words_found(stdscr, list_of_results, h, w,
                                       gamestate.score,
                                       len(gamestate.word_set))
                    update_words_found_int(stdscr, w,
                                           len(list_of_results) - results_corr)


if __name__ == '__main__':
    main()
