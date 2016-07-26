"""This is a blackjack game where the player can play against themselves. It generates a hand, takes in inputs of when
to hit or stay, and tells the player if they have busted or hit a 21."""


from hand import Hand
from card import Card
from deck import Deck


def set_up_game():
    """Creates deck, and sets up player with hand of two cards."""
    hand = Hand([])
    deck = Deck([])
    ordered_deck = deck.create_deck()
    shuffled_deck = ordered_deck.shuffle_deck()
    hand.card_list += [draw_card_from_deck(shuffled_deck), draw_card_from_deck(shuffled_deck)]
    print('Welcome to Blackjack Deathmatch. My name is Skynet, and I am your dealer. '
          'Your hand is {}, {}'.format(hand.card_list[0], hand.card_list[1]))
    return shuffled_deck, hand


def prompt_for_hit(hand, deck):
    """Prompts the user if they would like to hit, then runs hit player function if yes.
    """
    game_over = False
    while game_over is False:
        hit_prompt = input('Would you like to hit? (y/n) ')
        if hit_prompt == 'y':
            hit_player(hand, deck)
            score = hand.score_hand()
            if score >= 21:
                game_over = True
        if hit_prompt == 'n':
            game_over = True
    score = hand.score_hand()
    game_over_print(score)


def game_over_print(score):
    """Prints statements on game ending, based on final score.

    >>> score = 20
    >>> game_over_print(score)
    Alright, your final score is 20
    """
    if score > 21:
        print('You busted!')
    if score == 21:
        print('You got a blackjack!')
    print('Alright, your final score is {}'.format(score))


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
    """Main."""
    deck, hand = set_up_game()
    prompt_for_hit(hand, deck)

if __name__ == '__main__':
    main()
