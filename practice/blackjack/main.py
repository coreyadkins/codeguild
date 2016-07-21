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
    game_over = False
    hand.card_list += [draw_card_from_deck(deck)]
    hand.card_list += [draw_card_from_deck(deck)]
    print('Welcome to Blackjack Deathmatch. My name is Skynet, and I am your dealer. '
          'Your hand is {}, {}'.format(hand.card_list[0], hand.card_list[1]))
    return deck, hand


def prompt_for_hit(hand, deck):
    """Prompts the user if they would like to hit, then runs hit player function if yes."""
    hit_prompt = input('Would you like to hit? (y/n) ')
    if hit_prompt == 'y':
        hit_player(hand, deck)
    elif hit_prompt == 'n':
        score = score_hand(hand)
        print('Alright, your final score is {}'.format(score))
    score = score_hand(hand)
    game_over = check_score(score)
    if game_over == False and hit_prompt == 'y':
        print('Your new score is {}'.format(score))
        prompt_for_hit(hand, deck)


def check_score(score):
    if score > 21:
        print('Bust!')
        game_over = True
    elif score == 21:
        print('Blackjack!')
        game_over = True
    elif score < 21:
        game_over = False
    return game_over


def draw_card_from_deck(deck):
    """
    # Will set this up later to actually draw from deck. For now just generates a random card.

    """
    return deck.card_list.pop()


def hit_player(hand, deck):
    """Draws a card from the deck and adds to hand."""
    new_card = draw_card_from_deck(deck)
    hand.card_list += [new_card]
    is_deck_empty = check_deck_empty(deck)
    return hand, is_deck_empty


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


def check_deck_empty(deck):
    """Checks if the deck is empty, returns bool value if True"""
    if len(deck.card_list) == 0:
        is_deck_empty = True
    else:
        is_deck_empty = False
    return is_deck_empty


def main():
    deck, hand = set_up_game()
    prompt_for_hit(hand, deck)

if __name__ == '__main__':
    main()