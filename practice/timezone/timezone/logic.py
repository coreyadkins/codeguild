"""timezone Logic."""

import arrow
from tzwhere import tzwhere


def get_current_time():
    return arrow.utcnow().isoformat()

def get_timezone(lat, lng):
    lat, lng = float(lat), float(lng)
    tz = tzwhere.tzwhere()
    return tz.tzNameAt(lat, lng)

def get_time_at_timezone(timezone):
    current_time = arrow.utcnow()
    return current_time.to(timezone).isoformat()