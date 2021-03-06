"""timezone Logic."""

import arrow
from tzwhere import tzwhere


def get_current_time():
    """Returns the current time in UTC formatted for ISO 8601."""
    return arrow.utcnow()


def get_timezone(lat, lng):
    """Inputs latitude and longitude coordinates, outputs the name of the timezone at those coordinates.

    >>> get_timezone(43.068888, -121.008911)
    'America/Los_Angeles'
    >>> get_timezone(1, 1)
    Traceback (most recent call last):
        ...
    ValueError: Invalid coordinates
    """
    tz = tzwhere.tzwhere()
    timezone = tz.tzNameAt(lat, lng)
    if timezone is None:
        raise ValueError('Invalid coordinates')
    else:
        return timezone


def get_time_at_timezone(timezone):
    """Takes a timezone name, and gives the current time at that timezone."""
    current_time = arrow.utcnow()
    return current_time.to(timezone)

