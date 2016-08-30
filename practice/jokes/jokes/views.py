"""jokes Views."""

from . import models
from django.shortcuts import render
from django.http import HttpResponse

def render_index(request):
    arguments = {
        'jokes': models.jokes
    }
    return render(request, 'jokes/index.html', arguments)

def render_form(request):
    return render(request, 'jokes/form.html')

def render_submit_ack(request):
    try:
        setup = request.POST['setup']
        punchline = request.POST['punchline']
    except KeyError:
        return HttpResponse('Missing fields', status=400)
    models.add_new_joke(setup, punchline)
    return render(request, 'jokes/submit_ack.html')