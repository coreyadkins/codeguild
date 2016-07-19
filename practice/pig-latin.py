"""This program turns a word into pig latin"""
# 1. Define

def gather_user_input():
    """"Gathers word to be converted into pig latin from user"""
    input_word = input('Type word: ')
    return input_word

def transform_word_to_pig_latin(input_word):
    """Transforms the inputted word into pig latin"""
    VOWELS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if input_word_as_list[0] in VOWELS:
        pig_latin_word = ''.join(input_word) + 'yay'
    else:
        pig_latin_word = ''.join(input_word[1:]) + ''.join(input_word[0]) + 'ay'
    return pig_latin_word

def punctuate_word(pig_latin_word, input_word):
    """Properly punctuates a word"""
    pig_latin_word = pig_latin_word.lower()
    if  input_word[0].isupper():
        final_pig_latin_word = pig_latin_word.capitalize()
    else:
        final_pig_latin_word = pig_latin_word
    return final_pig_latin_word

# 2. Main

def main():
    input_word = gather_user_input()
    pig_latin_word = transform_word_to_pig_latin(input_word)
    punctuated_pig_latin_word = punctuate_word(pig_latin_word, input_word)
    print_statement = input_word + ' in Pig Latin is ' + punctuated_pig_latin_word
    print(print_statement)

main()


# 3. Input

# 4. Transform

# 5. Print