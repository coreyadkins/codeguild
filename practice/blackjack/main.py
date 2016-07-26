"""This is a blackjack game where the player can play against themselves. It generates a hand, takes in inputs of when
to hit or stay, and tells the player if they have busted or hit a 21."""


from hand import Hand
from card import Card
from deck import Deck
from random import shuffle

NAME_CARDS = ['j', 'q', 'k']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
SUITS = ['h', 'd', 's', 'c']
RANKS = NAME_CARDS + NUMBER_CARDS + ['a']


def set_up_game():
    """Creates deck, and sets up player with hand of two cards."""
    hand = Hand([])
    ordered_deck = create_deck()
    shuffled_deck = shuffle_deck(ordered_deck)
    hand.card_list += [draw_card_from_deck(shuffled_deck)]
    hand.card_list += [draw_card_from_deck(shuffled_deck)]
    print('Welcome to Blackjack Deathmatch. My name is Skynet, and I am your dealer. '
          'Your hand is {}, {}'.format(hand.card_list[0], hand.card_list[1]))
    return shuffled_deck, hand, game_over


def prompt_for_hit(hand, deck, game_over):
    """Prompts the user if they would like to hit, then runs hit player function if yes.
    """
    game_over = False
    while game_over is False:
        hit_prompt = input('Would you like to hit? (y/n) ')
        if hit_prompt == 'y':
            hit_player(hand, deck)
            score = score_hand(hand)
            game_over = check_score(score)
        elif hit_prompt == 'n':
            game_over = True
        if game_over is True:
            break
    if game_over is True:
        score = score_hand(hand)
        game_over_print(score)

def game_over_print(score):
    """Prints statements on game ending, based on final score.

    >>> score = 20
    >>> game_over_print(score)
    """
    if score > 21:
        print('You busted!')
    if score == 21:
        print('You got a blackjack!')
    print('Alright, your final score is {}'.format(score))


def check_score(score):
    """Checks the inputted score, determines if the score is a 'Bust!', 'Blackjack, if so, prints corresponding
    statements, then outputs a value on whether the game is over depending on the score.

    >>> check_score(22)
    True

    >>> check_score(21)
    True

    >>> check_score(20)
    False
    """
    if score > 21:
        game_over = True
    elif score == 21:
        game_over = True
    else:
        game_over = False
    return game_over


def draw_card_from_deck(deck):
    """Draws the 'top' card from an inputted deck, removes this card from the deck list.

    >>> deck = Deck([Card('c', '2')])
    >>> draw_card_from_deck(deck)
    Card('c', '2')
    >>> deck
    Deck([])
    """
    # return Card('s', '2')
    return deck.card_list.pop()


def hit_player(hand, deck):
    """Draws a card from the deck and adds to hand.

    >>> hit_player(Hand([Card('c', '2')]), Deck([Card('h', 'a')]))
    Hand([Card('c', '2'), Card('h', 'a')])
    >>> hit_player(Hand([Card('c', '2')]), Deck([Card('h', 'a'), Card('s', 'k')]))
    Hand([Card('c', '2'), Card('s', 'k')])
    """
    new_card = draw_card_from_deck(deck)
    hand.card_list += [new_card]
    return hand


def score_hand(hand):
    """Scores a given hand.

    >>> score_hand(Hand([Card('c', '2'), Card('s', 'k')]))
    12
    """
    score = sum(score_card(card) for card in hand.card_list)
    for card in hand.card_list:
        if card.rank == 'a' and score <= 11:
            score += 10
    return score


def score_card(card):
    """Scores a given card.

    >>> score_card(Card('c', 'a'))
    1
    >>> score_card(Card('h', 'k'))
    10
    >>> score_card(Card('s', '7'))
    7
    """
    if card.rank in NAME_CARDS:
        return 10
    elif card.rank in NUMBER_CARDS:
        return int(card.rank)
    else:
        return 1


def create_deck():
    """Creates and shuffles a new deck.

    >>> SUITS = ['c']
    >>> RANKS = ['2', '3', '4']
    >>> create_deck()
    Deck([Card('c', '2'), Card('c', '3'), Card('c', '4')])
    """
    deck = Deck([])
    for suit in SUITS:
        for rank in RANKS:
            new_card = Card(suit, rank)
            deck.card_list += [new_card]
    return deck


def shuffle_deck(deck):
    """Shuffles an ordered deck of cards."""
    return shuffle(deck.card_list)


# def check_deck_empty(deck):
#     """Checks if the deck is empty, returns bool value if True.
#     >>> check_deck_empty(Deck([]))
#     True
#     >>> check_deck_empty(Deck([Card('d', '2')]))
#     False
#     """
#     if len(deck.card_list) == 0:
#         is_deck_empty = True
#     else:
#         is_deck_empty = False
#     return is_deck_empty

# def pretty_print_cards():


def main():
    deck, hand, game_over = set_up_game()
    prompt_for_hit(hand, deck, game_over)

if __name__ == '__main__':
    main()
