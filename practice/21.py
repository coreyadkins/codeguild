"""This program dispenses Blackjack playing guidance"""
#1. Setup

NAME_CARDS = ['J', 'Q', 'K']
NUMBER_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

#2. input

first_card = input('What is your first card?')
second_card = input('What is your second card?')

#3. Transform

if first_card in NAME_CARDS:
    first_card_value = 10
if first_card in NUMBER_CARDS:
    first_card_value = int(first_card)
if first_card == 'A':
    first_card_value = 1
if second_card in NAME_CARDS:
    second_card_value = 10
if second_card in NUMBER_CARDS:
    second_card_value = int(first_card)
if second_card == 'A':
    second_card_value = 1

sum_card_values = first_card_value + second_card_value
if first_card == 'A' or second_card == 'A' and sum_card_values <= 11:
    sum_card_values += 10

# Determining Outputs (Note: Add functionality to input hit card)
if sum_card_values < 17:
    output = 'Hit!'
if sum_card_values >=17:
    output = 'Stay!'
if sum_card_values == 21:
    output = 'Blackjack!'

#4. Output
print(output)
