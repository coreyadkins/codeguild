"""multimadlib Models."""

from django.template import Template

_madlibs = [{'name': 'fred',
             'template': Template('{{noun}} is dumb.')}]

def access_all_madlibs():
    """Returns the global variable which stores all inputted madlibs."""
    return _madlibs


def access_madlib_by_name(name):
    """Returns the madlib which has the requested name."""
    for madlib in _madlibs:
        if madlib['name'] == name:
            return madlib


def template_is_valid(name, template):
    """Tests if the name or template in a new madlib template are not empty"""
    return len(name) > 0 and len(template) > 0


def create_new_madlib(name, template):
    """Creates a new madlib template using the Madlib class."""
    if template_is_valid(name, template):
        _madlibs.append({'name': name, 'template': template})
    else:
        raise KeyError('Missing fields')


# def completions_are_valid(country, adjective_1, noun_1):
#     """Checks if the inputted completions are not empty."""
#     return len(country) > 0 and len(adjective_1) > 0 and len(noun_1) > 0
#
#
# def add_completions_to_madlib(name, country, adjective_1, noun_1):
#     """Adds inputted completions to a selected madlib."""
#     if completions_are_valid(country, adjective_1, noun_1):
#         for madlib in _madlibs:
#             if madlib.name == name:
#                 madlib.add_completions(country, adjective_1, noun_1)
#
