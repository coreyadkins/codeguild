""'This program converts text from snake_case to CamelCase and from CamelCase to snake_case""'

# 1. Setup

def prompt_for_input_word():
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


def convert_to_correct_case(is_snake_case_bool, input_word):
    """Converts inputed word to CamelCase or snake_case based on which case it was in originally
    >>> convert_to_correct_case(CamelCase)
    camel_case
    """
    # Converting CamelCase to snake_case
    if is_snake_case_bool == False:
        input_word_list = list(input_word)
        capital_positions_indicies = [i for i, x in enumerate(input_word) if x.isupper()]
        word_with_underscores = [input_word_list.append('_') for x, capital_positions_indicies in enumerate(input_word_list)]
        # How to do no functions? I.e. [if x == 0 else none ...]
        () 
    None





        # for x in input_word_list:
        #     input_wrod
    # Converting snake_case to CamelCase
    # if is_snake_case_bool == True:


# 2. Define

# 3. Main

def main():
    input_word = prompt_for_input_word()
    is_snake_case_bool = detect_case(input_word)
    converted_word = convert_to_correct_case(is_snake_case_bool, input_word)
    print(converted_word)

if __name__ == '__main__':
    main()