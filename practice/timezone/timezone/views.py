"""timezone Views."""

from django.http import HttpResponse
from . import logic


def get_server_time(request):
    """Retrieves the current time in UTC 8601 format."""
    current_time = logic.get_current_time()
    return HttpResponse(current_time)


def get_timezone_at_lat_lng(request, lat, lng):
    """Retrieves the timezone name at inputted longitude and latitude coordinates.

    >>> X = get_timezone_at_lat_lng('request', '43.068888', '-121.008911')
    >>> X.content
    b'America/Los_Angeles'
    """
    timezone = logic.get_timezone(float(lat), float(lng))
    return HttpResponse(timezone)


def get_time_at_lat_lng(request, lat, lng):
    """Retrives the current time at inputted longitude and latitude coordinates."""
    timezone = logic.get_timezone(float(lat), float(lng))
    time_at_timezone = logic.get_time_at_timezone(timezone)
    return HttpResponse(time_at_timezone)


def convert_time_from_lat_lngs(request, in_time, out_lat, out_lng):
    """Converts inputted time into concurrent time at output longitude and latitude coordinates.

    >>> X = convert_time_from_lat_lngs('request', '2013-05-09T03:59:59.999999-04:00', '43.068888', '-121.008911')
    >>> X.content
    b'2013-05-09T00:59:59.999999-07:00'
    """
    timezone_out = logic.get_timezone(float(out_lat), float(out_lng))
    converted_time = logic.convert_to_timezone(in_time, timezone_out)
    return HttpResponse(converted_time)