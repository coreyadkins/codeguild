"""polls Logic."""

def total_votes(POLL):
    return sum(POLL.values())

def get_vote_percent(vote_total, flavor_votes):
    if vote_total == 0:
        return 0
    else:
        return flavor_votes / vote_total * 100

