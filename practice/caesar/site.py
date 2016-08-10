from string import ascii_uppercase


def get_key():
    """Returns the key for encryption as an int.

    May later contain an input function.
    """
    return 3


def get_input_word():
    """Returns the input word as an uppercase string.

    May later contain an input function.
    """
    return 'HOW ARE YOU'


def encrypt_word(key, input_word):
    i = 0
    output_list = []
    for input_letter in input_word:
        for letter in ascii_uppercase:
            if input_letter == letter:
                index = i + key
                if index > 25:
                    index -= 26
                output_list.append(ascii_uppercase[index])
            if i >= 25:
                if input_letter == ' ':
                    output_list.append(input_letter)
                i = 0
            else:
                i += 1
    return ''.join(output_list)


def caesarEncrypt():
    """Takes in a string and shifts it [key] amount on the alphabet to encrypt
    the word.
    >>> caesarEncrypt()
    'KRZ DUH BRX'
    """
    key = get_key()
    input_word = get_input_word()
    return encrypt_word(key, input_word)


def caesarDecrypt():
    """Takes in a string and shifts it back [key] amount on the alphabet to
    decrypt the word.
    """
