"""This module performs the functions for Tic-Tac-Toe (TTT) program of placing a token on the board, determining the
winner of a game, and returning a str version of the board, using tuples data type.
"""
from operator import itemgetter

WINNING_COMBINATIONS = [[(0, 0), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 1),
                                                                                                       (1, 2)],
                        [(2, 0), (2, 1), (2, 2)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1),
                                                                                                       (0, 2)]]


class CoordsTTTBoard:
    """Contains a blank TTT board as list of tuples items, and commands to modify the board, score game, and return str
    version of board.
    """
    def __init__(self):
        """Defines input value."""
        self._list_of_tokens = []

    def __repr__(self):
        """Returns real version.

        >>> repr(CoordsTTTBoard())
        'CoordsTTTBoard()'
        """
        return 'CoordsTTTBoard()'

    def __eq__(self, other):
        """Defines eauality.

        >>> CoordsTTTBoard() == CoordsTTTBoard()
        True
        """
        return self._list_of_tokens == other._list_of_tokens

    def place_token(self, x, y, token):
        """Adds token to a running list of tuples which represents board layout.

        >>> X = CoordsTTTBoard()
        >>> X.place_token(1, 1, 'X')
        >>> X._list_of_tokens
        [(1, 1, 'X')]
        """
        self._list_of_tokens.append(tuple([x, y, token]))

    def calc_winner(self):
        """Calculates what token character string has won or None if no one has.

        >>> X = CoordsTTTBoard()
        >>> X._list_of_tokens = [(1, 1, 'X'), (1, 0, 'X'), (1, 2, 'X'), (1, 1, 'O'), (2, 1, 'O')]
        >>> X.calc_winner()
        'X'
        >>> X = CoordsTTTBoard()
        >>> X._list_of_tokens = [(1, 0, 'X'), (1, 1, 'O'), (2, 1, 'X')]
        >>> X.calc_winner() is None
        True
        >>> X = CoordsTTTBoard()
        >>> X._list_of_tokens = [(1, 1, 'X'), (1, 0, 'X'), (1, 2, 'O'), (1, 1, 'O'), (2, 1, 'O')]
        >>> X.calc_winner() is None
        True
        """
        coords_to_token = {}
        key = itemgetter(0)
        winner = None
        for token in self._list_of_tokens:
            item = (token[2], (token[0], token[1]))
            coords = (token[0], token[1])
            group = key(item)
            if group not in coords_to_token:
                coords_to_token[group] = []
            coords_to_token[group].append(coords)
        for item in coords_to_token:
            if sorted(coords_to_token[item]) in WINNING_COMBINATIONS:
                winner = item
        return winner

    def __str__(self):
        """Returns a pretty-printed string of the board.

        >>> X = CoordsTTTBoard()
        >>> X._list_of_tokens = [(0, 2, 'X'), (2, 0, 'X'), (2, 2, 'O'), (1, 0, 'X'), (1, 2, 'O'), (1, 1, 'O'), \
                                (2, 1, 'O')]
        >>> print(X.__str__())
         |X|X
         |O|O
        X|O|O
        """
        row_1 = [' ', ' ', ' ']
        row_2 = [' ', ' ', ' ']
        row_3 = [' ', ' ', ' ']
        # x = itemgetter(0)
        # y = itemgetter(1)
        # token = itemgetter(2)
        for item in self._list_of_tokens:
            x = item[0]
            y = item[1]
            if y == 0:
                row_1[x] = item[2]
            if y == 1:
                row_2[x] = item[2]
            if y == 2:
                row_3[x] = item[2]
        row_1 = '|'.join(row_1)
        row_2 = '|'.join(row_2)
        row_3 = '|'.join(row_3)
        return str(row_1 + '\n'+ row_2 + '\n' + row_3)