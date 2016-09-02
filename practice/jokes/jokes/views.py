"""jokes Views."""

from . import logic
from django.shortcuts import render
from django.http import HttpResponse


def render_index(request):
    """Renders the index page which contains a list of all jokes."""
    arguments = {
        'jokes': logic.get_all_jokes(),
    }
    return render(request, 'jokes/index.html', arguments)


def render_form(request):
    """Renders the form for submitting jokes."""
    return render(request, 'jokes/form.html')


def render_submit_ack(request):
    """Renders the submit acknowledgment if a valid joke is entered on form, otherwise returns a 400 response."""
    try:
        setup = request.POST['setup']
        punchline = request.POST['punchline']
        logic.add_new_joke(setup, punchline)
    except ValueError:
        return HttpResponse('Missing fields', status=400)
    return render(request, 'jokes/submit_ack.html')
