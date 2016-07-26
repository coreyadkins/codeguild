"""Relates with functions and classes that function as the deck in Blackjack."""

from card import Card
from random import shuffle


NAME_CARDS = ['j', 'q', 'k']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
SUITS = ['h', 'd', 's', 'c']
RANKS = NAME_CARDS + NUMBER_CARDS + ['a']
TEST_SUITS = ['c']
TEST_RANKS = ['2', '3', '4']


class Deck:
    """This class represents a deck of cards, holding a list of Card class objects."""
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """Returns literal version of output.

        >>> repr(Deck([Card('spade', 'A'), Card('heart', 'J')]))
        "Deck([Card('spade', 'A'), Card('heart', 'J')])"
        """
        return 'Deck({!r})'.format(self.card_list)

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

    def create_deck(self, suits=SUITS, ranks=RANKS):
        """Creates and shuffles a new deck.

        >>> deck = Deck([])
        >>> deck.create_deck(TEST_SUITS, TEST_RANKS)
        Deck([Card('c', '2'), Card('c', '3'), Card('c', '4')])
        """
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.card_list += [new_card]
        return self

    def shuffle_deck(self):
        """Shuffles an ordered deck of cards."""
        return shuffle(self.card_list)
