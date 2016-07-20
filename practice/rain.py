"""This program reads a table containing all rainfall data for Sunnyside School, then prints out the specific date with
most rain, and the year with the most rain.
"""
# 1. Setup
import operator


# 2. Define

def import_table():
    """This imports the table to be read from the file"""
    with open('sunnysiderain.txt') as rain_table:
        intial_table = rain_table.readlines()
    stripped_table = strip_table(intial_table)
    return cut_out_items(stripped_table)

def strip_table(table):
    r"""Strips the table of formatting.

    >>> strip_table([''] * 12 + ['A \n'])
    [['A']]
    """
    return [line.strip().split() for line in table[12:]]

def cut_out_items(stripped_table):
    """Cuts out unused parts of the imported data.

    >>> cut_out_items([['A', 'B', 'C']])
    [['A', 'B']]
    """
    return [line[:2] for line in stripped_table]

def get_date_to_amt(table):
    """Turns data into a dictionary that pairs each date with the rainfall amount on that day.

    >>> get_date_to_amt([['A', '3']])
    {'A': 3}
    """
    date_to_amt = {key: value for (key, value) in table}
    return filter_table(date_to_amt)

def find_date_with_most_rain(date_to_amt):
    """Compares all dictionary items and returns the date with the highest value.

    >>> find_date_with_most_rain({'A': 1, 'B': 2})
    'B'
    """
    return max(date_to_amt.items(), key=operator.itemgetter(1))[0]

def filter_table(date_to_amt):
    """Removes dates which have no data from data set.

    >>> filter_table({'15-DEC-2010': '-', '24-JUL-2009': '0'})
    {'24-JUL-2009': 0}
    """
    return {date: int(amt) for date, amt in date_to_amt.items() if not '-' == amt}

def sort_table_by_year(date_to_amt):
    """Groups all values into new items based on the year of the data.

    >>> [(key, sorted(list_val)) for key, list_val in sorted(sort_table_by_year({'15-NOV-2009': 6, '08-JAN-2009': 0}).items())]
    [('2009', [0, 6])]
    """
    year_to_amts= {}
    for date, amt in date_to_amt.items():
        year = date[-4:]
        if year not in year_to_amts:
            year_to_amts[year] = []
        year_to_amts[year] += [amt]
    return year_to_amts

def find_year_with_most_rain(year_to_amts):
    """Compares all items and returns the year with the highest value.

    >>> find_year_with_most_rain({'2011': [0, 1, 2, 3], '2012': [2, 3, 4, 5]})
    '2012'
    """
    total_rain_by_year = sum_yearly_amounts(year_to_amts)
    return max(total_rain_by_year.items(), key=operator.itemgetter(1))[0]

def sum_yearly_amounts(year_to_amts):
    """Maps the dictionary and sums the values of all items.

    >>> sorted(sum_yearly_amounts({'2011': [0, 1, 2, 3], '2012': [2, 3, 4, 5]}).items())
    [('2011', 6), ('2012', 14)]
    """
    year_to_amts.update({key: sum(value) for key, value in year_to_amts.items()})
    return year_to_amts

def

# 3. Main

def main():
    table = import_table()
    date_to_amt = get_date_to_amt(table)
    date_with_most_rain = find_date_with_most_rain(date_to_amt)
    years_to_amts = sort_table_by_year(date_to_amt)
    year_with_most_rain = find_year_with_most_rain(years_to_amts)
    print('The date with most rain was {}' .format(date_with_most_rain))
    print('The year with the most rain {}' .format(year_with_most_rain))


if __name__ == '__main__':
    main()