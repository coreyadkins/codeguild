"""This program turns a word into pig latin"""
# Fix so that Capitalization reflects the input word, rather than just always
# capitalizing, or always punctuating.

# Separate grammar block from Pig Latin block.

# 1. Setup

VOWEL = ['a', 'e', 'i', 'o', 'u', 'A,' 'E', 'I', 'O', 'U']

# 2. Input

# english_word = input('Type word: ')
english_word = 'Cool'

# 3. Transform

english_word_as_list = list(english_word)

if english_word_as_list[0] in VOWEL:
    separated_first_letter = ''.join(english_word_as_list[0])
    punctuated_word_stem = (separated_first_letter.upper() +
                            ''.join(english_word_as_list[1:]))
    pig_latin_word = punctuated_word_stem + 'yay.'

else:
    pig_latin_word = ''.join(english_word_as_list[1]) + ''.join(english_word_as_list[2:]) + ''.join(english_word_as_list[0]) + 'ay'

# Punctualization block

pig_latin_word = pig_latin_word.lower()

if  english_word[0].isupper():
    print('True')
    final_pig_latin_word= pig_latin_word.capitalize()
else:
    final_pig_latin_word = pig_latin_word

english_word_first_letter_capitalized = ''.join(english_word_as_list[0])
english_word_punctuated = (english_word_first_letter_capitalized.upper() +
                          ''.join(english_word_as_list[1:]))

# 4. Output

print(english_word_punctuated + ' in Pig Latin is ' + final_pig_latin_word)
