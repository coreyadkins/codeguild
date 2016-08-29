"""polls Models."""

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
    POLL.update_poll(vote)


POLL = Poll(['chocolate', 'strawberry', 'vanilla'])


