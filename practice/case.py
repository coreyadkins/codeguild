""'This program converts text from snake_case to CamelCase and from CamelCase to snake_case""'

# 1. Setup
import re

# 2. Define

def prompt_for_input_phrase():
    """Gathers input word from user"""
    return input('What is the word you would like to transform? ')
    # return 'test_word'

def detect_case(input_word):
    """Detects whether the word is in snake_case or not, generates bool value storing this.

    >>> detect_case('test_word')
    True
    """
    is_snake_case = not input_word[0].isupper()
    return is_snake_case

def get_word_list(is_snake_case_bool, input_phrase):
    """This program inputs a bool identifying whether a phrase is in either snake_case or CamelCase, the phrase itself,
     and then splits the phrase into a list of words based on which case is used.

     >>> get_word_list(True, 'test_word')
     ['test', 'word']
     """
    word_list = re.findall('[A-Z][^A-Z]*', input_phrase) if is_snake_case_bool == False else input_phrase.split('_')
    return word_list

def convert_to_correct_case(is_snake_case_bool, list_of_words):
    """Inputs a list of words to convert either to snake_case or CamelCase based on the case of the inputted word.

    >>> convert_to_correct_case(False, ['Camel', 'Case'])
    'camel_case'
    >>> convert_to_correct_case(True, ['snake', 'case'])
    'SnakeCase'
    """
    if is_snake_case_bool == True:
        output_version = convert_to_camel_case(list_of_words)
    else:
        output_version = convert_to_snake_case(list_of_words)
    return output_version

def convert_to_camel_case(list_of_words):
    """Converts inputted words into CamelCase

    >>> convert_to_camel_case(['snake', 'case'])
    'SnakeCase'
    """
    upper_case_word = [x.capitalize() for x in list_of_words]
    return ''.join(upper_case_word)

def convert_to_snake_case(list_of_words):
    """Converts inputted words into snake_case

    >>> convert_to_snake_case(['Camel', 'Case'])
    'camel_case'
    """
    word_with_underscores = '_'.join(list_of_words)
    return word_with_underscores.lower()


# 3. Main

def main():
    input_phrase = prompt_for_input_phrase()
    is_snake_case_bool = detect_case(input_phrase)
    list_of_words = get_word_list(is_snake_case_bool, input_phrase)
    converted_word = convert_to_correct_case(is_snake_case_bool, list_of_words)
    print(converted_word)

if __name__ == '__main__':
    main()