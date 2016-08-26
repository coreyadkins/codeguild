"""pantheon Logic."""

from . import models

def get_people_by_code_and_industry(code, industry):
    people = [
        person
        for person in models.people
        if person['countryCode'].upper() == code and person['industry'].title() == industry
    ]
    return people
