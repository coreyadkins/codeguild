"""jokes Models."""

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup,
        self.punchline = punchline

    def __eq__(self, other):
        return self.setup == other.setup and self.punchline == other.punchline

    def __repr__(self):
        return 'Joke({!r},{!r})'.format(
            self.setup,
            self.punchline
        )


def add_new_joke(setup, punchline):
    jokes.append(Joke(setup, punchline))

jokes = []


