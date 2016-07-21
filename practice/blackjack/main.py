from hand import Hand
from card import Card
from deck import Deck
from random import shuffle
from dealer import dealer_hit_decision

NAME_CARDS = ['j', 'q', 'k']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
SUITS = ['h', 'd', 's', 'c']
RANKS = NAME_CARDS + NUMBER_CARDS + ['a']
PRETTY_SUITS = {'h': 'Hearts', 'd': 'Diamonds', 's': 'Spades', 'c':'Clubs'}
PRETTY RANKS = {'2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
                '9': 'Nine', '10': 'Ten', 'j': 'Jack', 'q': 'Queen', 'k': 'King', 'a': 'Ace'}

def set_up_game():
    """Creates deck, and sets up player with hand of two cards."""
    player_hand = Hand([])
    dealer_hand = Hand([])
    deck = create_deck()
    game_over = False
    player_hand.card_list += [draw_card_from_deck(deck)]
    player_hand.card_list += [draw_card_from_deck(deck)]
    dealer_hand.card_list += [draw_card_from_deck(deck)]
    dealer_hand.card_list += [draw_card_from_deck(deck)]
    print('Welcome to Blackjack Deathmatch. My name is Skynet, and I am your dealer. '
          'Your hand is {}, {}'.format(player_hand.card_list[0], player_hand.card_list[1]))
    return deck, player_hand, game_over, dealer_hand


def run_game(player_hand, deck, game_over, dealer_hand):
    """Prompts the user if they would like to hit, then runs hit player function if yes.
    # Split into smaller parts?
    """
    while game_over is False:
        hit_prompt = input('Would you like to hit? (y/n) ')
        if hit_prompt == 'y':
            hit_player(player_hand, deck)
            dealer_hand = dealer_calc_to_hit(dealer_hand, deck)
            player_score = score_hand(player_hand)
            game_over = check_score(player_score)
            dealer_score = score_hand(dealer_hand)
            if game_over is False:
                dealer_score = score_hand(dealer_hand)
                game_over = check_score(dealer_score)
            print('Your new card was {}. Your new hand is {}'.format(player_hand.card_list[-1], player_hand.card_list))
        elif hit_prompt == 'n':
            dealer_hand = dealer_calc_to_hit(dealer_hand, deck)
            game_over = True
    if game_over is True:
        player_wins = check_who_wins(player_score, dealer_score)
        if player_wins is True:
            print('You win!\nYour final score was {}. The dealers was {}. You survive this time..'
                  .format(player_score, dealer_score))
        elif player_wins is False:
            print('You lose!\nYour final score was {}. The dealers was {}. Prepare for termination.'
                  .format(player_score, dealer_score))
        elif player_wins is None:
            print('Push! Neither of us win? Does not compute..')


def dealer_calc_to_hit(dealer_hand, deck):
    """Calculates whether the dealer will hit, if the dealer does, hits.


    """
    dealer_score = score_hand(dealer_hand)
    does_dealer_hit = dealer_hit_decision(dealer_score)
    if does_dealer_hit is True:
        hit_player(dealer_hand, deck)
    return dealer_hand


def check_who_wins(player_score, dealer_score):
    """Checks the scores of player and dealer, returns the winner based on a bool"""
    if player_score > dealer_score:
        if player_score <= 21:
            player_wins = True
        elif player_score > 21:
            if dealer_score > 21:
                player_wins = None
            else:
                player_wins = False
    elif player_score < dealer_score:
        if dealer_score < 21:
            player_wins = False
        elif dealer_score > 21:
            if player_score > 21:
                player_wins = None
            else:
                player_wins = True
    elif player_score == dealer_score:
        player_wins = None
    return player_wins


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
        game_over = True
    elif score == 21:
        game_over = True
    else:
        game_over = False
    return game_over


def draw_card_from_deck(deck):
    """Draws the 'top' card from an inputted deck.

    >>> draw_card_from_deck(Deck([Card('c', '2')]))
    Card('c', '2')
    """
    # return Card('s', '8')
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

def pretty_print_cards(card):
    for card in hand.card_list:
        if card.suit in PRETTY_SUITS:
            pretty_card.suit =


def main():
    deck, player_hand, game_over, dealer_hand = set_up_game()
    run_game(player_hand, deck, game_over, dealer_hand)

if __name__ == '__main__':
    main()
