""'This program converts text from snake_case to CamelCase and from CamelCase to snake_case""'

# 1. Setup
import re

# 2. Define

def prompt_for_input_phrase():
    """Gathers input word from user"""
    # return input('What is the word you would like to transform?')
    return 'TestWord'

def detect_case(input_word):
    """Detects whether the word is in snake_case or not, generates bool value storing this
    >>> detect_case('test_word')
    True
    """
    if input_word[0].isupper() == True:
        is_snake_case = False
    else:
        is_snake_case = True
    return is_snake_case

def get_word_list(is_snake_case_bool, input_phrase):
    """This program inputs a bool identifying whether a phrase is in either snake_case or CamelCase, the phrase itself,
     and then splits the phrase into a list of words based on which case is used.
     >>> get_word_list(True, 'test_word')
     ['test', 'word']
     """
    if is_snake_case_bool == False:
        word_list = re.findall('[A-Z][^A-Z]*', input_phrase)
    if is_snake_case_bool == True:
        word_list = input_phrase.split('_')
    return word_list

def convert_to_correct_case(is_snake_case_bool, list_of_words):
    """Inputs a list of words to convert either to snake_case or CamelCase based on the case of the inputted word.
    >>> convert_to_correct_case(False, ['Camel', 'Case'])
    'camel_case'
    """
    if is_snake_case_bool == False:
        word_with_underscores = '_'.join(list_of_words)
        lower_case = word_with_underscores.lower()
        output_version = lower_case
    if is_snake_case_bool == True:
        upper_case_word = [x.capitalize() for x in list_of_words]
        joined_word = ''.join(upper_case_word)
        output_version = joined_word
    return output_version

# 3. Main

def main():
    input_phrase = prompt_for_input_phrase()
    is_snake_case_bool = detect_case(input_phrase)
    list_of_words = get_word_list(input_phrase)
    converted_word = convert_to_correct_case(is_snake_case_bool, list_of_words)
    print(converted_word)

if __name__ == '__main__':
    main()