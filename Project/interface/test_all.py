from .Gamestate import GameState
from woordenlijst.woordenlijst_filter import *


class TestGameState:
    def test_gamestate(self):
        state = GameState()
        state.letters = ['i', 'a', 't', 'l', 'd', 'f', 's']
        state.set_words()
        word_set = state.word_set
        assert len(word_set) == 40
        assert word_set == {'taffia', 'assist', 'taai', 'distillaat',
                            'stilist', 'fits', 'lila', 'lift', 'list',
                            'salafist', 'alias', 'altist', 'fatalist', 'flits',
                            'attila', 'titi', 'dadaist', 'distaal', 'stil',
                            'sadist', 'saldi', 'lidstaat', 'laai', 'fitis',
                            'staflid', 'tafia', 'alia', 'saai', 'fiat',
                            'ftisis', 'sisal', 'filiaal', 'tillift',
                            'sits', 'liflaf', 'lias', 'aids', 'stift',
                            'taaitaai', 'iliitis'}

        assert len(state.get_hint()) == 2
        assert state.is_correct("saai") == ['+1', 1]
        assert state.increase_score("staflid") == ['PANGRAM FOUND! +14', 14]


class TestWoordenlijstFilter:
    def test_woordenlijst_filter(self):
        assert len(pangrams()) == 2632
