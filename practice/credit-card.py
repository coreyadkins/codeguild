"""Program checks to see if a credit card number is valid."""

# 1. Define
def get_cc_number():
    """Asks user for a CC number."""
    user_cc_num = input('Please enter a credit card number to check. ')
    # user_cc_num = '4556737586899855'
    return user_cc_num

# math credit card number
def get_check_digit(user_cc_num):
    """"Returns the last digit from the cc number to check against
    >>> get_check_digit('12')
    '2'
    """
    return user_cc_num[-1]

def get_validation_digit(user_cc_num):
    """Generates a validation number from the cc number to check
    >>> get_validation_digit('4556737586899855')
    '5'
    """
    # 1. slice off last digit
    shortened_validation_digit = user_cc_num[:-1]

    # 2. reverse digits
    reversed_digit_list = reverse_digit_list(shortened_validation_digit)
    reversed_digits_as_ints = str_to_ints_in_list(reversed_digit_list)

    # 3. Multiply the odd reversed digits by two.
    multiplied_ints = multiply_even_index_ints(reversed_digits_as_ints)

    # 4. subtract nine from numbers > 9
    subtracted_ints = subtracting_large_ints(multiplied_ints)

    # 5. Sum all subtracted values.
    sum_values = sum(subtracted_ints)

    # 6. Take the 1s digit of that sum
    return str(sum_values % 10)

def str_to_ints_in_list(str_list):
    """Converts a list of str type expressions into a list of int type expressions
    >>> str_to_ints_in_list(['1', '2', '3'])
    [1, 2, 3]
    """
    int_list = [int(x) for x in str_list]
    return int_list

def multiply_even_index_ints(int_list):
    """Multiplies the even indexed numbers in a llist by 2, returns result in list
    >>> multiply_even_index_ints([1, 2, 3])
    [2, 2, 6]
    """
    return [x if i % 2 == 1 else x * 2 for i, x in enumerate(int_list)]
    # [x * 2 for i, x in enumerate(int_list) if is_odd(i)]


def subtracting_large_ints(int_list):
    """Subtracts 9 from any numbers larger than 9 in a list
    >>> subtracting_large_ints([10, 2, 6])
    [1, 2, 6]
    """
    return [x - 9 if x > 9 else x for x in int_list]


def reverse_digit_list(digits):
    """Reverses a string, outputs as list
    >>> reverse_digit_list('12345678')
    ['8', '7', '6', '5', '4', '3', '2', '1']
    """
    reversed_value = reversed(digits)
    return list(reversed_value)

def compare_values(first_value, second_value):
    """Checks on whether two values are equal, returns a boolean value
    >>> compare_values(1, 1)
    True
    """
    if first_value == second_value:
        is_valid = True
    else:
        is_valid = False
    return is_valid

def generate_validation_statement(is_card_valid_bool):
    """Generates print statment for output."""
    if is_card_valid_bool == True:
        output_statement = 'Valid!'
    else:
        output_statement = 'Invalid!'
    return output_statement

# 2. Main

def main():
    """Runs the program."""
    cc_num = get_cc_number()
    check_digit = get_check_digit(cc_num)
    validation_digit = get_validation_digit(cc_num)
    are_digits_equal = compare_values(check_digit, validation_digit)
    output_statement = generate_validation_statement(are_digits_equal)
    print(output_statement)

if __name__ == '__main__':
    main()

# 3. Output