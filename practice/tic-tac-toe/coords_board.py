class CoordsTTTBoard:
    def __init__(self, x, y, token):
        """Defines input value."""
        self.x = x
        self.y = y
        self.token = token

    def __repr__(self):
        """Returns real version.

        >>> repr(CoordsTTTBoard(0, 0, 'X'))
        "CoordsTTTBoard(0, 0, 'X')"
        """
        return 'CoordsTTTBoard({}, {}, {!r})'.format(
            self.x,
            self.y,
            self.token
        )

    def __eq__(self, other):
        """Defines eauality.

        >>> CoordsTTTBoard(0, 0, 'X') == CoordsTTTBoard(0, 0, 'X')
        True
        >>> CoordsTTTBoard(0, 0, 'X') == CoordsTTTBoard(0, 1, 'X')
        False
        """
        return (
            self.x == other.x and
            self.y == other.y and
            self.token == other.token
        )

    def place_token(self, x, y, token):
        """Adds token to a list of tuples which keeps track of token coordinates. Places a character string at a given coordinate,
        top left is 0, 0, x is horizontal position, y is vertical position.

        """

    def calc_winner():
        """Calculates what token character string has won or None if no one has.

        """

    def __str__():
        """Returns a pretty-printed picture of the board.

        """