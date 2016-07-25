class ListTTTBoard:
    def __init__(self, x, y, token):
        """Defines input value."""
        self.x = x
        self.y = y
        self.token = token

    def __repr__(self):
        """Returns real version.

        >>> repr(ListTTTBoard(0, 0, 'X'))
        "ListTTTBoard(0, 0, 'X')"add 
        """
        return 'ListTTTBoard({}, {}, {!r})'.format(
            self.x,
            self.y,
            self.token
        )

    def __eq__(self, other):
        """Defines eauality.

        >>> ListTTTBoard(0, 0, 'X') == ListTTTBoard(0, 0, 'X')
        True
        >>> ListTTTBoard(0, 0, 'X') == ListTTTBoard(0, 1, 'X')
        False
        """
        return (
            self.x == other.x and
            self.y == other.y and
            self.token == other.token
        )