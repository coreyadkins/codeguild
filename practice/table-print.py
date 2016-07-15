"""Prints a pretty version of an imported text table with columns"""
# 1. Setup

# 2. Transform


def read_in_file_as_rows():
    with open('table.txt', 'r') as table_file:
        initial_list = table_file.readlines()
    return initial_list

def table_in_columns(initial_list):
    num_columns = len(initial_list[0].split(' '))
    i = 0
    for row in initial_list:
        initial_list[i] = initial_list[i].strip()
        initial_list[i] = initial_list[i].split(' ')
        i += 1
    master_list = []
    for i in range(num_columns):
        master_list.append([])
    i = 0
    j = 0
    for line in initial_list:
        for j in range(num_columns):
            master_list[j].append(initial_list[i][j])
        i += 1
    return master_list

def measure_columns(text_in_columns):
    length_list = []
    i = 0
    for i in range(len(text_in_columns)):
        for word in (text_in_columns[i]):
            word_lengths = []
            word_lengths.append(len(word))
        length_list.append(max(word_lengths))
    return length_list

def pad_table(table, length_list):
    """
    >>> pad_table([['Apple', 'Banana'],['VW', 'Ford']], [6, 4])
    [['Apple ', 'Banana'], ['VW  ', 'Ford']]

    :param table:
    :param length_list:
    :return:
    """
    #formatted_table = [add_spaces(word, length_list[i]) for i in range(len(table)) for word in table[i]],


    x = list(zip(table, length_list))
    y = list(zip(length_list, table))
    formatted_table = [pad_column(column, pad_length) for column, pad_length in x]
    return formatted_table

def boarder_table(table_as_columns, length_list):
    x = list(zip(table_as_columns, length_list))
    table_with_borders = [boarder_column(column, length) for column, length in x]
    return table_with_borders

def add_pipes_to_table(table):
    """
    >>> add_pipes_to_table([['Apple ', 'Banana'], ['VW  ', 'Ford']])
    [['|Apple ', '|Banana'], ['|VW  |', '|Ford|']]

    :param table:
    :return:
    """
    piped_table = [add_pipe_to_column(column) for column in table]

    piped_table[-1] = [word + '|' for word in piped_table[-1]]
    return piped_table


def add_pipe_to_column(column):
    """
    >>> add_pipe_to_column(['Apple ', 'Banana'])
    ['|Apple ', '|Banana']

    :param column:
    :return:
    """
    piped_column = [add_pipe_to_word(word) for word in column]
    return piped_column


def add_pipe_to_word(word):
    """
    >>> add_pipe_to_word('apple')
    '|apple'

    :param word:
    :return:
    """
    return '|' + word


def boarder_column(column, column_size):
    dashes = ['-' * column_size]
    new_column = dashes + column + dashes
    return new_column

def pretty_print(table):
    x = list(zip(*table))
    [print(''.join(row)) for row in x]


def pad_column(column, length):
    """
    >>> pad_column(['apple', 'banana', 'pear'], 6)
    ['apple ', 'banana', 'pear  ']

    :param column:
    :param length:
    :return:
    """
    new_column = [add_spaces(word, length) for word in column]
    return new_column





def add_spaces(word, length_column):
    """
    >>> add_spaces('apple', 6)
    'apple '

    :param word:
    :param length_column:
    :return:
    """
    return_word = word.ljust(length_column)
    return return_word
    # return word.ljust(length_column)

# def border()



# 3. Main

def main():
    initial_list = read_in_file_as_rows()
    text_in_columns = table_in_columns(initial_list)
    length_list = measure_columns(text_in_columns)
    padded_table = pad_table(text_in_columns, length_list)
    bordered_table = boarder_table(padded_table, length_list)
    piped_table = add_pipes_to_table(bordered_table)
    pretty_print(piped_table)

if __name__ == "__main__":
    main()