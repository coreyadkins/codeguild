"""Relates to functions and classes that work with individual cards in the blackjack deck."""

NAME_CARDS = ['j', 'q', 'k']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']


class Card:
    """This class represents a single card in a deck, holding their suit type and rank as strs."""
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

    def score_card(self):
        """Scores a given card.

        >>> card = Card('c', 'a')
        >>> card.score_card()
        1
        >>> card = Card('h', 'k')
        >>> card.score_card()
        10
        >>> card = Card('s', '7')
        >>> card.score_card()
        7
        """
        if self.rank in NAME_CARDS:
            return 10
        elif self.rank in NUMBER_CARDS:
            return int(self.rank)
        else:
            return 1
