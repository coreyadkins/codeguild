"""polls Logic."""

from . import models


class Poll:
    def __init__(self, flavors):
        self.votes = {flavor: 0 for flavor in flavors}

    def __repr__(self):
        return 'Polls({!r})'.format(
            self.flavors
        )

    def __eq__(self, other):
        return (
            self.flavors == other.flavors
        )
    def update_poll(self, vote):
            self.votes[vote] += 1



def update_poll(vote):
    models.POLL.update_poll(vote)


def get_poll(vote):
    """

    """
    vote_total = sum(models.POLL.votes.values())
    poll_data = {flavor: get_poll_item(models.POLL.votes[flavor], vote_total) for flavor in models.POLL.votes}
    return poll_data


def get_poll_item(flavor_votes, vote_total):
    return {
        'votes': flavor_votes,
        'percent': flavor_votes / vote_total * 100
    }