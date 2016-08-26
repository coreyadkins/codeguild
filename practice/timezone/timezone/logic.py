"""timezone Logic."""

import arrow
from tzwhere import tzwhere


def get_current_time():
    """Returns the current time in UTC formatted for ISO 8601."""
    return arrow.utcnow().isoformat()


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
    return current_time.to(timezone).isoformat()


def convert_to_timezone(time_in, timezone_out):
    """Takes a time and date, converts the time to the time at output timezone."

    :param time_in: Starting time and date
    :param timezone_out: Timezone name of output timezone
    :return: Arrow object converted to new timezone

    >>> convert_to_timezone('2013-05-09T03:59:59.999999-04:00', 'America/Los_Angeles')
    <Arrow [2013-05-09T00:59:59.999999-07:00]>
    >>> convert_to_timezone('Bob', 'America/Los_Angeles')
    Traceback (most recent call last):
        ...
    ValueError: Invalid time
    """
    try:
        time_in = arrow.get(time_in)
        return time_in.to(timezone_out)
    except arrow.parser.ParserError:
        raise ValueError('Invalid time')

