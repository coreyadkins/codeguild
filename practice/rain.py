"""This program reads a table containing all rainfall data for Sunnyside School, then prints out the specific date with
most rain, and the year with the most rain.
"""
# 1. Setup
import operator


# 2. Define

def import_table():
    with open('sunnysiderain.txt') as rain_table:
        initial_list = rain_table.readlines()
    stripped_table = strip_table(initial_list)
    return cut_out_items(stripped_table)

def strip_table(table):
    r"""
    >>> strip_table([''] * 12 + ['A \n'])
    [['A']]

    :param table:
    :return:
    """
    return [line.strip().split() for line in table[12:]]

def cut_out_items(stripped_table):
    """
    >>> cut_out_items([['A', 'B', 'C']])
    [['A', 'B']]

    :param stripped_table:
    :return:
    """
    return [line[:2] for line in stripped_table]

def make_lookup_table(formatted_table):
    """
    >>> make_lookup_table([['A', 'B']])
    {'A': 'B'}

    :param formatted_table:
    :return:
    """
    return {key: value for (key, value) in formatted_table}

def find_date_with_most_rain(filtered_table):
    """
    >>> find_date_with_most_rain({'A': '1', 'B': '2'})
    B

    :param lookup_table:
    :return:
    """
    return max(filtered_table.items(), key=operator.itemgetter(1))[0]

def filter_table(lookup_table): # Check to make sure this works
    """
    >>> filter_table({'15-DEC-2010': '-', '24-JUL-2009': '0'})
    {'24-JUL-2009': '0'}
    :param lookup_table:
    :return:
    """
    return {date: int(amt) for date, amt in lookup_table.items() if not '-' == amt}

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

def sort_table_by_year(date_to_amt): # Sexier solution- slice off date and month, then sort into buckets based on year key, look at grouping solution on notes
    year_to_amts= {}
    for date, amt in date_to_amt.items():
        year = date[-4:]
        if year not in year_to_amts:
            year_to_amts[year] = []
        year_to_amts[year] += [amt]
    return year_to_amts

def find_year_with_most_rain(year_to_amts):
    total_rain_by_year = sum_yearly_amounts(year_to_amts)
    return max(total_rain_by_year.items(), key=operator.itemgetter(1))[0]

def sum_yearly_amounts(year_to_amts):
    return {item[year:, sum(amts)] for item[year:, amts] in year_to_amts.items()}


# total_rain_by_year = {}
# for item in year_to_amts.items():
#     for year, amts in item:
#         if year not in total_rain_by_year:
#             total_rain_by_year[year] = []
#         total_rain_by_year[year] += sum[amts]

# 3. Main

def main():
    table = import_table()
    lookup_table = make_lookup_table(table)
    filtered_table = filter_table(lookup_table)
    date_with_most_rain = find_date_with_most_rain(filtered_table)
    table_sorted_by_year = sort_table_by_year(filtered_table)
    year_with_most_rain = find_year_with_most_rain(table_sorted_by_year)
    print('The date with most rain was {}' .format(date_with_most_rain))
    print('The year with the most rain {}' .format(year_with_most_rain))


if __name__ == '__main__':
    main()