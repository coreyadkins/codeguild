"""This module performs the functions for Tic-Tac-Toe (TTT) program of placing a token on the board, determining the
winner of a game, and returning a str version of the board, using list data type.
"""


class ListTTTBoard:
    """Contains a blank TTT board as list items, and commands to modify the board, score game, and return str version
    of board.
    """
    def __init__(self):
        """Defines input value."""
        self._rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __repr__(self):
        """Returns real version.

        >>> repr(ListTTTBoard())
        'ListTTTBoard()'
        """
        return 'ListTTTBoard()'

    def __eq__(self, other):
        """Defines eauality.

        >>> ListTTTBoard() == ListTTTBoard()
        True
        """
        return self._rows == other._rows

    def place_token(self, x, y, token):
        """Adds token to a running list which represents board layout. Places a character string at a given coordinate,
        top left is 0, 0, x is horizontal position, y is vertical position.

        >>> X = ListTTTBoard()
        >>> X.place_token(1, 1, 'X')
        >>> X._rows
        [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
        """
        self._rows[y][x] = token

    def calc_winner(self):
        """Calculates what token character string has won or None if no one has.

        >>> X = ListTTTBoard()
        >>> X._rows = [['O', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X.calc_winner()
        'O'
        >>> X = ListTTTBoard()
        >>> X._rows = [['X', 'O', ' '], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X.calc_winner()
        'X'
        >>> X = ListTTTBoard()
        >>> X._rows = [['Y', 'O', ' '], ['X', 'Y', 'O'], [' ', 'O', 'Y']]
        >>> X.calc_winner()
        'Y'
        """
        _test_list = self._create_test_list()
        winner = _check_for_winner(_test_list)
        return winner

    def __str__(self):
        """Returns a pretty-printed string of the board.

        >>> X = ListTTTBoard()
        >>> X._rows = [['O', 'O', 'O'], ['X', ' ', 'X'], ['X', 'O', 'O']]
        >>> print(X.__str__())
        O|O|O
        X| |X
        X|O|O
        """
        joined_rows = ['|'.join(row) for row in self._rows]
        return '\n'.join(joined_rows)

    def _create_test_list(self):
        """Creates a list of lists which contain all possible winning permutations to check against.

        >>> X = ListTTTBoard()
        >>> X._rows = [['O', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X._create_test_list()
        [['O', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', ' '], ['O', 'X', 'X'], ['O', 'X', 'O'], ['O', 'O', ' '], ['O', 'X\
', ' '], ['O', 'X', 'X']]
        """
        return self._rows + self._table_as_columns() + self._table_as_diags()

    def _table_as_columns(self):
        """Returns table sorted into rows as table sorted into columns.

        >>> X = ListTTTBoard()
        >>> X._rows = [['X', 'O', ' '], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X._table_as_columns()
        [['X', 'X', 'X'], ['O', 'X', 'O'], [' ', 'O', ' ']]
        """
        columns = [[], [], []]
        for row in self._rows:
            for item in range(len(row)):
                columns[item].append(row[item])
        return columns

    def _table_as_diags(self):
        """Returns table sorted into rows as two lists which represent the two diagonal axis on the TTT Board.

        >>> X = ListTTTBoard()
        >>> X._rows = [['Y', 'O', ' '], ['X', 'Y', 'O'], [' ', 'O', 'Y']]
        >>> X._table_as_diags()
        [['Y', 'Y', 'Y'], [' ', 'Y', ' ']]
        """
        diags = [[], []]
        i = 0
        for rows in self._rows:
            diags[0].append(rows[i])
            i += 1
        i = 2
        for rows in self._rows:
            diags[1].append(rows[i])
            i -= 1
        return diags


def _check_for_winner(iterable):
    """Checks whether a given list of items wins the game, meaning that all strs in the item are equivalent.

    >>> lists = [['X', 'X', 'X'], ['X', 'O', ' '], ['X', 'O', 'O']]
    >>> _check_for_winner(lists)
    'X'

    >>> lists = [['X', 'O', 'X'], [' ', ' ', ' '], ['X', 'O', 'O']]
    >>> _check_for_winner(lists) is None
    True

    Filters out blank space giving a false positive.
    """
    winner = None
    for item in iterable:
        if len(set(item)) <= 1:
            winner = item[0]
            if winner == ' ':
                winner = None
    return winner