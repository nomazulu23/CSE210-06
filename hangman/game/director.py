from puzzle import Puzzle


class Director:
    def __init__(self):
        self._puzzle = Puzzle()
        self._is_playing = True

    def start_game(self):
        while self._is_playing:
            self._getInputs()
            self._updates()

    def _getInputs(self):
        self._puzzle.letter()

    def _updates(self):
        self._puzzle.end_game()
        if self._puzzle._validate == 1:
            self._is_playing = False
        elif self._puzzle._validate == 2:
            self._is_playing = False
