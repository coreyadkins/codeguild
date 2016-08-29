"""polls Views."""

from django.shortcuts import render
from . import logic
from . import models

def render_summary(request):
    arguments = {
        'flavors': logic.get_poll()
    }
    return render(request, 'polls/summary.html', arguments)

def render_forms_ack(request):
    vote = request.POST['flavor']
    models.update_poll(vote)
    return render(request, 'polls/forms_ack.html')

def render_form(request):
    arguments ={
        'flavors': models.POLL.votes.keys()
    }
    return render(request, 'polls/poll_form.html', arguments)
