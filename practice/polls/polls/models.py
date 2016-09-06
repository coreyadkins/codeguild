"""polls Models."""


POLL = {'chocolate': 0, 'strawberry': 0, 'vanilla': 0}

def add_vote_to_poll(vote):
    POLL[vote] += 1


