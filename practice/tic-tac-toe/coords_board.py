"""This module performs the functions for Tic-Tac-Toe (TTT) program of placing a token on the board, determining the
winner of a game, and returning a str version of the board, using tuples data type.
"""
from operator import itemgetter


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
        self._list_of_tokens.append((x, y, token))

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
        key = itemgetter(0)
        winning_combinations = _get_winning_combinations()
        winner = None
        tokens_to_coords = [(token[2], (token[0], token[1])) for token in self._list_of_tokens]
        coords_to_token = _group_by(tokens_to_coords, key)
        for token in coords_to_token:
            if sorted(coords_to_token[token]) in winning_combinations:
                winner = token
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
        print_list = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
        for token in self._list_of_tokens:
            x = token[0]
            y = token[1]
            print_list[y][x] = token[2]
        joined_rows = ['|'.join(row) for row in print_list]
        return '\n'.join(joined_rows)


def _get_winning_combinations():
    """Generates all of the possible winning combinations in a tic tac toe board."""
    winning_col_combinations = [[(x, y) for y in range(3)] for x in range(3)]
    winning_row_combinations = [[(x, y) for x in range(3)] for y in range(3)]
    winning_diag_combinations = [(i, i) for i in range(3)] + [(3 - i, i) for i in range(3)]
    return winning_col_combinations + winning_row_combinations + winning_diag_combinations


def _group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item[1])
    return group_to_items
