"""pantheon Views."""

from . import logic
from django.shortcuts import render
from django.http import HttpResponse


def get_countries(request):
    # http://localhost:8000/
    """ be quiet """
    countries = logic.get_unique_countries()
    return HttpResponse(countries)
