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
    deck = create_deck()
    game_over = False
    hand.card_list += [draw_card_from_deck(deck)]
    hand.card_list += [draw_card_from_deck(deck)]
    print('Welcome to Blackjack Deathmatch. My name is Skynet, and I am your dealer. '
          'Your hand is {}, {}'.format(hand.card_list[0], hand.card_list[1]))
    return deck, hand, game_over


def prompt_for_hit(hand, deck, game_over):
    """Prompts the user if they would like to hit, then runs hit player function if yes.
    # Split into smaller parts?
    """
    while game_over is False:
        # hit_prompt = input('Would you like to hit? (y/n) ')
        hit_prompt = 'n'
        if hit_prompt == 'y':
            hit_player(hand, deck)
            score = score_hand(hand)
            game_over = check_score(score)
            print('Your new score is {}'.format(score))
        elif hit_prompt == 'n':
            score = score_hand(hand)
            print('Alright, your final score is {}'.format(score))
            game_over = True
        if game_over is True:
            break
    if game_over is True:
        print('Game over!')


def check_score(score):
    """Checks the inputted score, determines if the score is a 'Bust!', 'Blackjack, if so, prints corresponding
    statements, then outputs a value on whether the game is over depending on the score.

    >>> check_score(22)
    Bust!
    True

    >>> check_score(21)
    Blackjack!
    True

    >>> check_score(20)
    False
    """
    if score > 21:
        print('Bust!')
        game_over = True
    elif score == 21:
        print('Blackjack!')
        game_over = True
    else:
        game_over = False
    return game_over


def draw_card_from_deck(deck):
    """Draws the 'top' card from an inputted deck.

    >>> draw_card_from_deck(Deck([Card('c', '2')]))
    Card('c', '2')
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
            score += 10
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
