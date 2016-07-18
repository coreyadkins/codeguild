"""This program reads a table containing all rainfall data for Sunnyside School, then prints out the specific date with
most rain, and the year with the most rain.
"""
# 1. Setup
import operator

def import_table():
    with open('sunnysiderain.txt', 'r') as rain_table:
        initial_list = rain_table.readlines()
    return initial_list

def strip_table(table):
    r"""
    >>> strip_table([''] * 12 + ['A \n'])
    [['A']]

    :param table:
    :return:
    """
    stripped_table = [line.strip().split() for line in table[12:]]
    return stripped_table

def cut_out_items(stripped_table):
    """
    >>> cut_out_items([['A', 'B', 'C']])
    [['A', 'B']]

    :param stripped_table:
    :return:
    """
    cut_table = [line[:2] for line in stripped_table]
    return cut_table

def make_lookup_table(formatted_table):
    """
    >>> make_lookup_table([['A', 'B']])
    {'A': 'B'}

    :param formatted_table:
    :return:
    """
    lookup_table = {key: value for (key, value) in formatted_table}
    return lookup_table



def find_date_with_most_rain(filtered_table):
    """
    >>> find_date_with_most_rain({'A': '1', 'B': '2'})
    B

    :param lookup_table:
    :return:
    """
    date_with_most_rain = max(filtered_table.items(), key=operator.itemgetter(1))[0]
    print(date_with_most_rain)
    return date_with_most_rain

def filter_table(lookup_table): # Check to make sure this works
    days_without_value = find_days_without_value(lookup_table)
    corrected_days = correct_days_without_value(days_without_value)
    lookup_table.update(corrected_days)
    return lookup_table

# def filter_table(lookup_table):
#     """
#     >>> filter_table({'15-DEC-2010': '-', '24-JUL-2009': '0'})
#     {'A': '1'}
#
#     :param lookup_table:
#     :return:
#     """
#     days_without_value = find_days_without_value(lookup_table)
#     filtered_table = {lookup_table.pop(item) for item in list(lookup_table) if item in list(days_without_value.keys())}
#     return filtered_table


def find_days_without_value(lookup_table):
    """
    >>> find_days_without_value({'15-DEC-2010': '-', '24-JUL-2009': '0'})
    {'B': '-'}

    :param lookup_table:
    :return:
    """
    days_without_value = {k: v for k, v in lookup_table.items() if '-' in v}
    return days_without_value

def correct_days_without_value(days_without_value):
    for key in days_without_value:
        days_without_value[key] = '0'
    return days_without_value

def sort_table_by_year(filtered_table): # Find a sexier solution.
    table_sorted_by_year = [[][][][][][][][][][][][][][][]]
    for key in filtered_table:
        if key[10:11] == '02':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '03':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '04':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '05':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '06':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '07':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '08':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '09':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '10':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '11':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '12':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '13':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '14':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '15':
            table_sorted_by_year[0] += [key]
        if key[10:11] == '16':
            table_sorted_by_year[0] += [key]
# 2. Define


# 3. Main

def main():
    table = import_table()
    stripped_table = strip_table(table)
    cut_table = cut_out_items(stripped_table)
    lookup_table = make_lookup_table(cut_table)
    filtered_table = filter_table(lookup_table)
    date_with_most_rain = find_date_with_most_rain(filtered_table)
    table_sorted_by_year = sort_table_by_year(filtered_table)


if __name__ == '__main__':
    main()