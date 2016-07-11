"""This program turns a word into pig latin"""

# 1. Setup

VOWEL = ['a', 'e', 'i', 'o', 'u']

# 2. Input

input_word = input('Type word: ')

# 3. Transform
input_word = input_word.lower()
split_word_list = list(input_word)

# Check first letter type, if consonant. Else, vowel. Use bool variable.

if split_word_list[0] in VOWEL:
    is_vowel = True
else:
    is_vowel = False

# Processing. Use if blocks against bool variable for consonant check. If true,
# transform by moving first letter to end, adding 'ay'. If false, add 'yay'

capitalization_input = ''.join(split_word_list[0])
input_word = capitalization_input.upper() + ''.join(split_word_list[1:])

if is_vowel is True:
    capitalization_input = ''.join(split_word_list[0])
    split_word_list = capitalization_input.upper() + ''.join(split_word_list[1:])
    pig_latin_word = split_word_list + 'yay.'

else:
    first_letter = split_word_list[0]
    capitalization_input = ''.join(split_word_list[1])
    split_word_list = capitalization_input.upper() + ''.join(split_word_list[2:])
    pig_latin_word = (''.join(split_word_list[1].upper()) +
                      ''.join(split_word_list[2:]) + first_letter + 'ay.')

# Capitalization and punctuation

# 4. Output

print(input_word + ' in Pig Latin is ' + pig_latin_word)
