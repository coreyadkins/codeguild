"""This program dispenses Blackjack playing guidance"""
# 1. Define

def prompt_user_input():
    first_card = input('What is your first card? ')
    second_card = input('What is your second card? ')
    submitted_cards_list = []
    submitted_cards_list += [first_card] + [second_card]
    return submitted_cards_list

def add_card_values(submitted_cards_list):
    NAME_CARDS = ['J', 'Q', 'K', 'j', 'q', 'k']
    NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    if submitted_cards_list[0] in NAME_CARDS:
        first_card_value = 10
    elif submitted_cards_list[0] in NUMBER_CARDS:
        first_card_value = int(submitted_cards_list[0])
    elif submitted_cards_list[0] == 'A':
        first_card_value = 1
    if submitted_cards_list[1] in NAME_CARDS:
        second_card_value = 10
    elif submitted_cards_list[1] in NUMBER_CARDS:
        second_card_value = int(submitted_cards_list[1])
    elif submitted_cards_list[1] == 'A':
        second_card_value = 1
    sum_of_card_values = first_card_value + second_card_value
    if submitted_cards_list[0] == 'A' or submitted_cards_list[1] == 'A' and sum_of_card_values <= 11:
        sum_of_card_values += 10
    return sum_of_card_values

def determine_output_suggestion(sum_of_card_values):
    if sum_of_card_values < 16:
        output_suggestion = 'Hit!'
    elif sum_of_card_values >= 17:
        output_suggestion = 'Stay!'
    elif sum_of_card_values == 21:
        output_suggestion = 'Blackjack!'
    return output_suggestion


# 2. Main

def main():
    submitted_cards_list = prompt_user_input()
    sum_of_card_values = add_card_values(submitted_cards_list)
    output_suggestion = determine_output_suggestion(sum_of_card_values)
    print(output_suggestion)
    return output_suggestion

main()

# 3. Input

# 4. Transform

# 5. Output
