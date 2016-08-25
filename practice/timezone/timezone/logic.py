"""timezone Logic."""

import arrow
from tzwhere import tzwhere


def get_current_time():
    """Returns the current time in UTC formatted for ISO 8601."""
    return arrow.utcnow().isoformat()


def get_timezone(lat, lng):
    """Inputs latitude and longitude coordinates, outputs the name of the timezone at those coordinates.

    >>> get_timezone('43.068888', '-121.008911')
    'America/Los_Angeles'
    """
    lat, lng = float(lat), float(lng)
    tz = tzwhere.tzwhere()
    return tz.tzNameAt(lat, lng)


def get_time_at_timezone(timezone):
    """Takes a timezone name, and gives the current time at that timezone."""
    current_time = arrow.utcnow()
    return current_time.to(timezone).isoformat()


def get_timezone_and_time(time, timezone):
    """Takes a date and time and a timezone name, turns data into an arrow object representing this info.

    >>> get_timezone_and_time('2013-05-09T03:59:59.999999', 'America/New_York')
    <Arrow [2013-05-09T03:59:59.999999-04:00]>
    """
    return arrow.get(time).replace(tzinfo=timezone)


def convert_to_timezone(time_in_with_timezone, timezone_out):
    """Takes an arrow time object, converts the time to the time at output timezone."

    :param time_in_with_timezone: Arrow object of starting time
    :param timezone_out: Timezone name of output timezone
    :return: Arrow object converted to new timezone

    >>>convert_to_timezone(<Arrow [2013-05-09T03:59:59.999999-04:00]>, 'America/Los_Angeles')
    <Arrow [2013-05-09T00:59:59.999999-07:00]>
    """
    return time_in_with_timezone.to(timezone_out)
