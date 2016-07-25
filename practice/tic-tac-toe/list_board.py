class ListTTTBoard:
    def __init__(self):
        """Defines input value."""
        self._rows = [['', '', ''], ['', '', ''], ['', '', '']]
        self._columns = [[], [], []]

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
        [['', '', ''], ['', 'X', ''], ['', '', '']]
        """
        self._rows[y][x] = token

    def table_as_columns(self):
        """Returns table sorted into rows as table sorted into columns.

        >>> X = ListTTTBoard()
        >>> X._rows = [['X', 'O', ''], ['X', 'X', 'O'], ['X', 'O', '']]
        >>> X.table_as_columns()
        >>> X._columns
        [['X', 'X', 'X'], ['O', 'X', 'O'], ['', 'O', '']]
        """
        for row in self._rows:
            for item in range(len(row)):
                self._columns[item].append(row[item])

    def calc_winner(self):
        """Calculates what token character string has won or None if no one has.

        >>> X = ListTTTBoard()
        >>> X._rows = [['O', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', '']]
        >>> X.calc_winner()
        'O'
        >>> X = ListTTTBoard()
        >>> X._rows = [['X', 'O', ''], ['X', 'X', 'O'], ['X', 'O', '']]
        >>> X.calc_winner()
        'X'

        >>> X = ListTTTBoard()
        >>> X._rows = [['Y', 'O', ''], ['X', 'Y', 'O'], ['', 'O', 'Y']]
        >>> X.calc_winner()
        'Y'
        """
        winner = None
        for y in self._rows:
            if len(set(y)) <= 1:
                winner = y[0]
            if winner == '':
                winner = None
            if winner != None:
                return winner
            else:
                winner = None
        self.table_as_columns()
        for x in self._columns:
            for y in x:
                if len(set(y)) <= 1:
                    winner = y
                else:
                    winner = None
            if winner == '':
                winner = None
            if winner != None:
                return winner
        if len(set(self._rows[0][0] and self._rows[1][1] and
                   self._rows[2][2])) <= 1 or len(set(self._rows[2][0] and self._rows[1][1] and self._rows[0][2])) <= 1:
            winner = self._rows[1][1]
            if winner == '':
                winner = None
            if winner != None:
                return winner
        else:
            winner = None
        return winner


    def __str__():
        """Returns a pretty-printed picture of the board.

        """