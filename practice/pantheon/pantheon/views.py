"""pantheon Views."""

from . import logic
from django.shortcuts import render
from . import models

def get_countries_and_country_ids(request):
    # http://localhost:8000/
    """ be quiet """
    arguments = {
        'countries': models.COUNTRY_CODE_TO_COUNTRY
    }
    return render(request, 'pantheon/index.html', arguments)

def get_industries_and_cur_ids(request, country_code):
    """"""
    arguments = {
        'industries': models.COUNTRY_CODE_TO_INDUSTRY[country_code]
    }
    return render(request, 'pantheon/industries.html', arguments)


def get_people_in_industry(request, country_code, industry):
    arguments = {
        'people': logic.get_people_by_code_and_industry(country_code, industry)
    }

    return render(request, 'pantheon/people.html', arguments)