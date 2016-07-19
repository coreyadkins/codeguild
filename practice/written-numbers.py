"""Converts a numeric number to written out English"""

num = int(input('Input a number < 99: '))

tens = num // 10
ones = number % 10

if ones == 9:
    ones_word = 'nine'
elif ones == 8:
    ones_word = 'eight'
elif ones == 7:
    ones_word = 'seven'
elif ones == 6:
    ones_word = 'six'
elif ones == 5:
    ones_word = 'five'
elif ones == 4:
    ones_word = 'four'
elif ones == 3:
    ones_word = 'three'
elif ones == 2:
    ones_word = 'two'
elif ones == 1:
    ones_word = 'one'

if tens == 0:
    output = ones_word
elif tens == 1:
    if ones == 1:
        output = 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    else:
        output = ones_word + 'teen'



print(output)
