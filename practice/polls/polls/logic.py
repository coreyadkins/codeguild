"""polls Logic."""

from . import models

def get_poll():
    """

    """
    vote_total = sum(models.POLL.votes.values())
    poll_data = [get_poll_item(models.POLL.votes[flavor], vote_total, flavor) for flavor in models.POLL.votes]
    return poll_data


def get_poll_item(flavor_votes, vote_total, flavor):
    if vote_total == 0:
        percent_number = 0
    else:
        percent_number = flavor_votes / vote_total * 100
    return {
        'votes': flavor_votes,
        'percent': percent_number,
        'flavor_name': flavor
    }

