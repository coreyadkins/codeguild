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
        {'X': (0, 0)}
        """
        token_as_dict = dict(key=token, value=[(x, y)])
        key = token_as_dict.keys()
        self.append_to_tokens_to_coords(token_as_dict, key)

    def calc_winner(self):
        """Calculates what token character string has won or None if no one has.

        """

    def __str__(self):
        """Returns a pretty-printed string of the board.

        """
