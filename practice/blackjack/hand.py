"""Relates with functions and classes that represent the hand in Blackjack"""

from card import Card


class Hand:
    """This class represents a hand of cards, holding a list of Card class objects."""
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """Returns literal version of output.

        >>> repr(Hand([Card('spade', 'A'), Card('heart', 'J')]))
        "Hand([Card('spade', 'A'), Card('heart', 'J')])"
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

    def score_hand(self):
        """Scores a given hand.
        >>> hand = Hand([Card('c', '2'), Card('s', 'k')])
        >>> hand.score_hand()
        12
        """
        score = sum(card.score_card() for card in self.card_list)
        for card in self.card_list:
            if card.rank == 'a' and score <= 11:
                score += 10
        return score
