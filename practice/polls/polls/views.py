"""polls Views."""

from django.shortcuts import render
from . import logic
from . import models

def render_summary(request):
    vote_total = logic.total_votes(models.POLL)
    poll_results_by_flavor = [{'flavor_name': flavor, 'percent': logic.get_vote_percent(vote_total, votes)} for flavor, votes in models.POLL.items()]
    arguments = {
        'results_by_flavor': poll_results_by_flavor
    }
    return render(request, 'polls/summary.html', arguments)

def render_forms_ack(request):
    vote = request.POST['flavor']
    models.add_vote_to_poll(vote)
    return render(request, 'polls/forms_ack.html')

def render_form(request):
    arguments ={
        'flavors': models.POLL.keys()
    }
    return render(request, 'polls/poll_form.html', arguments)
