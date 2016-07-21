from hand import Hand
from card import Card
from deck import Deck
from random import shuffle

NAME_CARDS = ['j', 'q', 'k']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
SUITS = ['h', 'd', 's', 'c']
RANKS = NAME_CARDS + NUMBER_CARDS + ['a']


# Set up variables for suits and ranks
# Use shuffle function to shuffle deck after creating deck

def set_up_game():
    """Creates deck, and sets up player with hand of two cards.
    """
    hand = Hand([])
    deck = create_deck()
    hand.card_list += [draw_card_from_deck(deck)]
    hand.card_list += [draw_card_from_deck(deck)]
    return deck, hand


def create_deck():
    return create_deck()


def draw_card_from_deck(deck):
    """
    # Will set this up later to actually draw from deck. For now just generates a random card.

    """
    return deck.card_list.pop()


def hit_player(hand, deck):
    """Draws a card from the deck and adds to hand."""
    new_card = draw_card_from_deck(deck)
    hand.card_list += [new_card]
    return hand


def score_hand(hand):
    """Scores a given hand."""
    score = 0
    for card in hand.card_list:
        if card.rank in NAME_CARDS:
            score += 10
        elif card.rank in NUMBER_CARDS:
            score += int(card.rank)
        else:
            score += 1
    for card in hand.card_list:
        if card.rank == 'a' and score <= 11:
            score += 11
    return score


def create_deck():
    """Creates and shuffles a new deck."""
    deck = Deck([])
    for suit in SUITS:
        for rank in RANKS:
            new_card = Card(suit, rank)
            deck.card_list += [new_card]
    shuffle(deck.card_list)
    return deck


def is_deck_empty():

    

def main():
    # Add a card to a hand
    deck, hand = set_up_game()
    print('Your hand is {}, {}'.format(hand.card_list[0], hand.card_list[1]))
    if_hit = hit_player(hand, deck)
    # Score a hand
    hand_score = score_hand(hand)
    print(hand_score)
    print(len(deck.card_list))
    # Return if the score is over 21
    # Allow a user to type in a hand and have it be converted into a Hand object
    # Return a new deck that is shuffled
    # Draw a card off the top of the deck
    # Return if the deck is empty
    pass

if __name__ == '__main__':
    main()