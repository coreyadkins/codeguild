"""pantheon Logic."""

from . import models


def get_unique_countries():
    """ """
    unique = set([person['countryName'].title() for person in models.people])
    return sorted(unique)
