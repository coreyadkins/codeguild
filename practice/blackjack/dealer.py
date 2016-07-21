def dealer_hit_decision(score):
    """This takes the total value of the two cards and generates a suggestion to hit, stay, or blackjack"""
    if score <= 16:
        dealer_hit = True
    elif score >= 17:
        dealer_hit = False
    return dealer_hit

