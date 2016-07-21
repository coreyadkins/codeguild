from card import Card

class Deck:
    """This class holds the list of all possible cards in a deck"""
    def __init__(self, card_list):
        self.card_list = card_list


    def __repr__(self):
        """Returns literal version of output.

        >>> repr(Deck([Card('spade', 'A'), Card('heart', 'J')]))
        "Deck([Card('spade', 'A'), Card('heart', 'J')])"
        """
        return 'Deck({!r})'.format(
            self.card_list
        )


    def __eq__(self, other):
        """Defines equality.

        >>> Deck([Card('spade', 'A'), Card('heart', 'J')]) == Deck([Card('spade', 'A'), Card('heart', 'J')])
        True
        >>> Deck([Card('spade', 'A'), Card('heart', 'J')]) == Deck([Card('spade', '2'), Card('heart', '10')])
        False
        """
        return (
            self.card_list == other.card_list
        )
