"""This program turns a word into pig latin"""
# 1. Define

def user_input():
    """"Gathers word to be converted into pig latin from user"""
    input_word = input('Type word: ')
    return input_word

def word_into_list(input_word):
    """Transforms a word into a list"""
    input_word_as_list = list(input_word)
    return input_word_as_list

def transform_word_to_pig_latin(input_word_as_list):
    """Transforms the inputted word into pig latin"""
    VOWEL = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if input_word_as_list[0] in VOWEL:
        pig_latin_word = ''.join(input_word_as_list) + 'yay'
    else:
        pig_latin_word = ''.join(input_word_as_list[1:]) + ''.join(input_word_as_list[0]) + 'ay'
    print(pig_latin_word)
    return pig_latin_word

def punctuate_word(pig_latin_word, input_word_as_list):
    """Properly punctuates a word"""
    pig_latin_word = pig_latin_word.lower()
    if  input_word_as_list[0].isupper():
        final_pig_latin_word = pig_latin_word.capitalize()
    else:
        final_pig_latin_word = pig_latin_word
    return final_pig_latin_word

# 2. Main

def main():
    input_word = user_input()
    input_word_as_list = word_into_list(input_word)
    pig_latin_word = transform_word_to_pig_latin(input_word_as_list)
    punctuated_pig_latin_word = punctuate_word(pig_latin_word, input_word_as_list)
    print_statement = input_word + ' in Pig Latin is ' +punctuated_pig_latin_word
    print(print_statement)
    return print_statement

main()


# 3. Input

# 4. Transform

# 5. Print