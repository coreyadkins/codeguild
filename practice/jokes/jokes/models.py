"""jokes Models."""

class Joke:
    """Class type that represents a joke.

    Includes a setup and a punchline.
    """
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __eq__(self, other):
        return self.setup == other.setup and self.punchline == other.punchline

    def __repr__(self):
        return 'Joke({}, {})'.format(
            self.setup,
            self.punchline
        )


def get_jokes():
    """Returns all jokes in submitted order."""
    return jokes


def joke_is_valid(setup, punchline):
    """Tests if both setup and punchline fields in submitted joke have a value."""
    return len(setup) > 0 and len(punchline) > 0


def add_new_joke(setup, punchline):
    """If joke is valid, adds joke as a Joke class object to global variable containing all jokes."""
    if joke_is_valid(setup, punchline):
        jokes.append(Joke(setup, punchline))
    else:
        raise ValueError('missing fields in joke')

jokes = [Joke('What time did the man go to the dentist?', 'Tooth hurt-y.'),
         Joke('Why do chicken coops only have two doors?', 'Because if they had four, they would be chicken sedans!')]


