class ListTTTBoard:
    def __init__(self):
        """Defines input value."""
        self._rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self._columns = [[], [], []]
        self._diags = [[], []]

    def __repr__(self):
        """Returns real version.

        >>> repr(ListTTTBoard())
        'ListTTTBoard()'
        """
        return 'ListTTTBoard()'

    def __eq__(self, other):
        """Defines eauality.

        >>> ListTTTBoard() == ListTTTBoard()
        (True, True)
        """
        return (
            self._rows == other._rows,
            self._columns == other._columns
        )

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
        >>> X = ListTTTBoard()
        >>> X._rows = [[' ', ' ', ' '], ['X', ' ', 'O'], [' ', 'O', 'X']]
        >>> X.calc_winner() is not None
        True
        """
        winner = None
        for row in self._rows:
            if len(set(row)) <= 1:
                winner = row[0]
            if winner == ' ':
                winner = None
            if winner is not None:
                return winner
            else:
                winner = None
        self.table_as_columns()
        for column in self._columns:
            if len(set(column)) <= 1:
                winner = column[0]
            else:
                winner = None
            if winner == ' ':
                winner = None
            if winner is not None:
                return winner
        self.table_as_diags()
        for diag in self._diags:
            if len(set(diag)) <= 1:
                winner = diag[0]
            if winner == ' ':
                winner = None
            if winner is not None:
                return winner
        return winner

    def __str__(self):
        """Returns a pretty-printed picture of the board.

        >>> X = ListTTTBoard()
        >>> X._rows = [['O', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X.__str__()
        O|O|O
        X|X|O
        X|O|
        """
        for row in self._rows:
            joined_row = '|'.join(row)
            print(joined_row)

    def table_as_columns(self):
        """Returns table sorted into rows as table sorted into columns.

        >>> X = ListTTTBoard()
        >>> X._rows = [['X', 'O', ' '], ['X', 'X', 'O'], ['X', 'O', ' ']]
        >>> X.table_as_columns()
        >>> X._columns
        [['X', 'X', 'X'], ['O', 'X', 'O'], [' ', 'O', ' ']]
        """
        for row in self._rows:
            for item in range(len(row)):
                self._columns[item].append(row[item])

    def table_as_diags(self):
        """Creates two lists which represent the diaganol axis on the TTT Board.

        >>> X = ListTTTBoard()
        >>> X._rows = [['Y', 'O', ' '], ['X', 'Y', 'O'], [' ', 'O', 'Y']]
        >>> X.table_as_diags()
        >>> X._diags
        [['Y', 'Y', 'Y'], [' ', 'Y', ' ']]
        """
        self._diags[0].append(self._rows[0][0])
        self._diags[0].append(self._rows[1][1])
        self._diags[0].append(self._rows[2][2])
        self._diags[1].append(self._rows[0][2])
        self._diags[1].append(self._rows[1][1])
        self._diags[1].append(self._rows[2][0])
li