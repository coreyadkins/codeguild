"""This module performs the functions for Tic-Tac-Toe (TTT) program of placing a token on the board, determining the
winner of a game, and returning a str version of the board, using dict data type.
"""

WINNING_COMBINATIONS = [[(0, 0), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 1),
                                                                                                       (1, 2)],
                        [(2, 0), (2, 1), (2, 2)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1),
                                                                                                       (0, 2)]]

class DictTTTBoard:
    """Contains a blank TTT board as dict items, and commands to modify the board, score game, and return str version
    of board.
    """
    def __init__(self):
        """Defines input value."""
        self._tokens_to_coords = {}

    def __repr__(self):
        """Returns real version.

        >>> repr(DictTTTBoard())
        'DictTTTBoard()'
        """
        return 'DictTTTBoard()'

    def __eq__(self, other):
        """Defines eauality.

        >>> DictTTTBoard() == DictTTTBoard()
        True
        """
        return self._tokens_to_coords == other._tokens_to_coords

    def place_token(self, x, y, token):
        """Uses grouping to add token as a new key item in a dictionary, all coordinates associating with that token are
        stored in the value as a list of tuples.

        >>> X = DictTTTBoard()
        >>> X.place_token(0, 0, 'X')
        >>> X._tokens_to_coords
        {'X': [(0, 0)]}
        """
        coords = (x, y)
        key = token
        self._append_to_tokens_to_coords(key, coords)

    def calc_winner(self):
        """Calculates what token character string has won or None if no one has.

        >>> X = DictTTTBoard()
        >>> X._tokens_to_coords = {'X': [(0, 0), (1, 0), (2, 0)]}
        >>> X.calc_winner()
        'X'
        >>> X = DictTTTBoard()
        >>> X._tokens_to_coords = {'X': [(0, 0), (1, 0)]}
        >>> X.calc_winner() is None
        True
        """
        winner = None
        for item in self._tokens_to_coords:
            if sorted(self._tokens_to_coords[item]) in WINNING_COMBINATIONS:
                winner = item
        return winner

    def __str__(self):
        """Returns a pretty-printed string of the board.

        >>> X = DictTTTBoard()
        >>> X._tokens_to_coords = {'X': [(0, 0), (1, 0), (2, 0)]}, {'O': [(0, 1), (2, 1), (2, 2)]}
        >>> print(X.__str__())
        X|X|X
        O| |O
         | |O
        """
        row_1 = [' ', ' ', ' ']
        row_2 = [' ', ' ', ' ']
        row_3 = [' ', ' ', ' ']
        i = 0
        for item in self._tokens_to_coords:
            for key, value in self._tokens_to_coords[i].items():
                for coord in value:
                    x = coord[0]
                    y = coord[1]
                    if y == 0:
                        row_1[x] = key
                    if y == 1:
                        row_2[x] = key
                    if y == 2:
                        row_3[x] = key
            i += 1
        row_1 = '|'.join(row_1)
        row_2 = '|'.join(row_2)
        row_3 = '|'.join(row_3)
        return str(row_1 + '\n' + row_2 + '\n' + row_3)

    def _append_to_tokens_to_coords(self, key, coords):
        group = key
        if group not in self._tokens_to_coords:
            self._tokens_to_coords[group] = []
        self._tokens_to_coords[group].append(coords)
