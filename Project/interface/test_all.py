from .Gamestate import GameState


class TestGameState:
    def test_gamestate_1(self):
        state = GameState()
        state.letters = ['i', 'a', 't', 'l', 'd', 'f', 's']
        word_set = state.word_set
        assert len(word_set) == 39
        assert word_set == {'fatalist', 'fits', 'taaitaai', 'filiaal', 'laai', 'stil',
                            'tillift', 'tafia', 'taffia', 'titi', 'taai', 'stilist',
                            'saldi', 'attila', 'salafist', 'flits', 'ftisis', 'lila',
                            'altist', 'sits', 'iliitis', 'stift', 'sadist', 'saai',
                            'liflaf', 'distillaat', 'alias', 'list', 'fitis', 'assist',
                            'staflid', 'lift', 'lias', 'fiat', 'distaal', 'lidstaat',
                            'alia', 'aids', 'sisal'}
