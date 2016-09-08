"""jokes Models."""


class Joke:
    """Class type that represents a joke.

    Includes a setup and a punchline.
    """
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        """Returns str.

        >>> str(Joke('Hello', 'Goodbye'))
        'Joke(Hello, Goodbye)'
        """
        return 'Joke({}, {})'.format(
            self.setup,
            self.punchline
        )

    def __eq__(self, other):
        """Tests equality.

        >>> (
        ... Joke('Hello', 'Goodbye') ==
        ... Joke('Hello', 'Goodbye')
        ... )
        True
        >>> (
        ... Joke('Hello', 'Goodbye') ==
        ... Joke('Hello', 'Yellow')
        ... )
        False
        """
        return self.setup == other.setup and self.punchline == other.punchline

    def __repr__(self):
        """Returns repr.

        >>> repr(Joke('Hello', 'Goodbye'))
        "Joke('Hello', 'Goodbye')"
        """
        return 'Joke({!r}, {!r})'.format(
            self.setup,
            self.punchline
        )

jokes = [Joke('What time did the man go to the dentist?', 'Tooth hurt-y.'),
         Joke('Why do chicken coops only have two doors?', 'Because if they had four, they would be chicken sedans!')]
