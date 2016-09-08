"""jokes Logic."""

from . import models


def get_all_jokes():
    """Returns all jokes in submitted order.

    >>> models.jokes = [models.Joke('Setup', 'Punchline')]
    >>> get_all_jokes()
    [Joke('Setup', 'Punchline')]
    """
    return models.jokes


def joke_is_valid(setup, punchline):
    """Tests if both setup and punchline fields in submitted joke have a value.

    >>> joke_is_valid('Setup', 'Punchline')
    True
    >>> joke_is_valid('Setup', '')
    False
    """
    return setup != '' and punchline != ''


def create_new_joke(setup, punchline):
    """Creates a new Joke class object to contain inputted joke.

    >>> create_new_joke('Setup', 'Punchline')
    Joke('Setup', 'Punchline')
    """
    return models.Joke(setup, punchline)


def append_joke(joke):
    """Appends a joke to the global Joke variable which contains all Jokes.

    >>> models.jokes = []
    >>> joke = models.Joke('Setup', 'Punchline')
    >>> append_joke(joke)
    >>> models.jokes
    [Joke('Setup', 'Punchline')]
    """
    models.jokes.append(joke)

def add_new_joke(setup, punchline):
    """Piping function for adding a new joke.

    Tests if inputted joke contains necessary fields, if it does, stores it in new instance in the Joke class, then
    appends it to the global variable which contains all inputted jokes.

    If the inputted joke is missing a field, raises a ValueError.

    >>> models.jokes = []
    >>> add_new_joke('Setup', 'Punchline')
    >>> models.jokes
    [Joke('Setup', 'Punchline')]
    >>> models.jokes = []
    >>> add_new_joke('Setup', '')
    Traceback (most recent call last):
    ...
    ValueError: missing fields in joke
    """
    if joke_is_valid(setup, punchline):
        joke = create_new_joke(setup, punchline)
        append_joke(joke)
    else:
        raise ValueError('missing fields in joke')
