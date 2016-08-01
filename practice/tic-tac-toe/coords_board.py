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
        list_0 = [' ', ' ', ' ']
        list_1 = [' ', ' ', ' ']
        list_2 = [' ', ' ', ' ']
        # x = itemgetter(0)
        # y = itemgetter(1)
        # token = itemgetter(2)
        for item in self._list_of_tokens:
            x = item[0]
            if item[1] == 0:
                list_0[x] = item[2]
            if item[1] == 1:
                list_1[x] = item[2]
            if item[1] == 2:
                list_2[x] = item[2]
        list_0 = '|'.join(list_0)
        list_1 = '|'.join(list_1)
        list_2 = '|'.join(list_2)
        return str(list_0 + '\n'+ list_1 + '\n' + list_2)




def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items