from card import Card

class Hand:
    """This class holds list of values of cards in hand"""
    def __init__(self, card_list):
        self.card_list = card_list


    def __repr__(self):
        """Returns literal version of output.

        >>> repr(Hand([Card('spade', 'A'), Card('heart', 'J')]))
        "Card([Card('spade', 'A'), Card('heart', 'J')])"
        """
        return 'Hand({!r})'.format(
            self.card_list
        )


    def __eq__(self, other):
        """Defines equality.

        >>> Hand([Card('spade', 'A'), Card('heart', 'J')]) == Hand([Card('spade', 'A'), Card('heart', 'J')])
        True
        >>> Hand([Card('spade', 'A'), Card('heart', 'J')]) == Hand([Card('spade', '2'), Card('heart', '10')])
        False
        """
        return (
            self.card_list == other.card_list
        )
