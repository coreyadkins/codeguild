"""Reformats a phone number into XXX-XXX-XXXX or same in parenthesis"""

# 1. Setup

# 2. Define

def gather_phone_number():
    """Requests user to enter a phone number, outputs it as string"""
    phone_str = input('Phone number? All digits. ')
    return phone_str

def reformat_phone_number(phone_number_as_string):
    """Reformats a phone number into format with dashes or same in parenthesis"""
    has_area_code = len(phone_number_as_string) > 7
    if has_area_code:
        phone_parts = [phone_number_as_string[:3], phone_number_as_string[3:6], phone_number_as_string[6:]]
    else:
        phone_parts = [phone_number_as_string[:3], phone_number_as_string[3:]]
    dashed_phone = '-'.join(phone_parts)
    if has_area_code:
        fancy_phone = '({}) {}-{}'.format(phone_parts[0], phone_parts[1], phone_parts[2])
    else:
        fancy_phone = dashed_phone
    output_phone_numbers = []
    output_phone_numbers = [fancy_phone] + [dashed_phone]
    return output_phone_numbers



# 3. Main
def main():
    phone_number_as_string = gather_phone_number()
    output_phone_numbers = reformat_phone_number(phone_number_as_string)
    print(' '.join(output_phone_numbers))
    return output_phone_numbers


main()



# #1. Setup
# # No setup!
#
# # 2. input
# phone_str = input('Phone number? All digits. ')
#
# # 3. Transform
#
# has_area_code = len(phone_str) > 7 # Boolean operator that returns True or False
#
# if has_area_code:
#     phone_parts = [phone_str[:3], phone_str[3:6], phone_str[6:]]
# else:
#     phone_parts = [phone_str[:3], phone_str[3:]]
#
# dashed_phone = '-'.join(phone_parts)
# if has_area_code:
#     fancy_phone = '({}) {}-{}'.format(phoneparts[0], phone_parts[1], phone_parts[2])
# else:
#      fancy_phone = dashed_phone
#
# # 4. Output
# print(dashed_phone)
# print(fancy_phone)
