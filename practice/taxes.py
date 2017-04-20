"""This program takes the user income and calculates and prints their total
income tax.
"""
# 1. Setup
OREGON_BRACKETS = [(3350, 0.05), (5050, 0.07), (116000, 0.09), (None, 9.9)]

# 2. input


def input_tax_information():
    """This gathers income and tax bracket information from the user."""
    income = float(input('What is your taxable income for the year?'))
    oregon_or_custom_bracket = str(input('Would you like to use the' +
    'Oregon tax bracket or input a custom one? Please input "Oregon" or' +
    '"Custom"'))
    if oregon_or_custom_bracket == 'Custom':
        is_progressive = str(input('Is this bracket progressive?'))
    else:
         tax_bracket = OREGON_BRACKETS
    return [income, tax_bracket]
# 3. Transform

# 4. Output
