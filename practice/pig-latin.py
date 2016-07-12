"""This program turns a word into pig latin"""
# 1. Setup

VOWEL = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

# 2. Input

english_word = input('Type word: ')

# 3. Transform

english_word_as_list = list(english_word)

if english_word_as_list[0] in VOWEL:
    pig_latin_word = ''.join(english_word_as_list) + 'yay'
else:
    pig_latin_word = ''.join(english_word_as_list[1:]) + ''.join(english_word_as_list[0]) + 'ay'

# Punctualization block

pig_latin_word = pig_latin_word.lower()

if  english_word[0].isupper():
    final_pig_latin_word = pig_latin_word.capitalize()
    final_english_word = english_word.capitalize()
else:
    final_pig_latin_word = pig_latin_word
    final_english_word = english_word


# 4. Output

print(final_english_word + ' in Pig Latin is ' + final_pig_latin_word)
