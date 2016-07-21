class Card:
    """This class holds card values"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        """Returns literal version of output.

        >>> repr(Card('spade', 'A'))
        "Card('spade', 'A')"
        """
        return 'Card({!r}, {!r})'.format(
            self.suit,
            self.rank
        )
    def __eq__(self, other):
        """Defines equality.

        >>> Card('Spade', 'A') == Card('Spade', 'A')
        True
        >>> Card('Spade', 'A') == Card('Heart', 'Q')
        False
        """
        return (
            self.suit == other.suit and
            self.rank == other.rank
        )
