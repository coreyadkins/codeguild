"""This module performs the functions for Tic-Tac-Toe (TTT) program of placing a token on the board, determining the
winner of a game, and returning a str version of the board, using dict data type.
"""


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
        winning_combinations = _get_winning_combinations()
        for token in self._tokens_to_coords:
            if sorted(self._tokens_to_coords[token]) in winning_combinations:
                winner = token
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
        print_list = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
        i = 0
        for token in self._tokens_to_coords:
                for key, value in self._tokens_to_coords[i].items():
                    for coord in value:
                        x = coord[0]
                        y = coord[1]
                        print_list[y][x] = key
                i += 1
        joined_rows = ['|'.join(row) for row in print_list]
        return '\n'.join(joined_rows)

    def _append_to_tokens_to_coords(self, key, coords):
        """Uses a group_by function to append a token to a dictionary of tokens and coordinates."""
        group = key
        if group not in self._tokens_to_coords:
            self._tokens_to_coords[group] = []
        self._tokens_to_coords[group].append(coords)


def _get_winning_combinations():
    """Generates all of the possible winning combinations in a tic tac toe board."""
    winning_col_combinations = [[(x, y) for y in range(3)] for x in range(3)]
    winning_row_combinations = [[(x, y) for x in range(3)] for y in range(3)]
    winning_diag_combinations = [(i, i) for i in range(3)] + [(3 - i, i) for i in range(3)]
    return winning_col_combinations + winning_row_combinations + winning_diag_combinations

