"""jokes Logic."""

from . import models


def get_all_jokes():
    """Returns all jokes in submitted order."""
    return models.jokes


def joke_is_valid(setup, punchline):
    """Tests if both setup and punchline fields in submitted joke have a value."""
    return len(setup) > 0 and len(punchline) > 0


def add_new_joke(setup, punchline):
    """If joke is valid, adds joke as a Joke class object to global variable containing all jokes."""
    if joke_is_valid(setup, punchline):
        models.jokes.append(models.Joke(setup, punchline))
    else:
        raise ValueError('missing fields in joke')
