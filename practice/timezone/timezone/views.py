"""timezone Views."""

from django.http import HttpResponse
from . logic import get_current_time, get_timezone, get_time_at_timezone, get_timezone_and_time, convert_to_timezone


def get_server_time(request):
    """Retrieves the current time in UTC 8601 format."""
    current_time = get_current_time()
    return HttpResponse(current_time)


def get_timezone_at_lat_lng(request, lat, lng):
    """Retrieves the timezone name at inputted longitude and latitude coordinates."""
    timezone = get_timezone(lat, lng)
    return HttpResponse(timezone)


def get_time_at_lat_lng(request, lat, lng):
    """Retrives the current time at inputted longitude and latitude coordinates."""
    timezone = get_timezone(lat, lng)
    time_at_timezone = get_time_at_timezone(timezone)
    return HttpResponse(time_at_timezone)


def convert_time_from_lat_lngs(request, in_lat, in_lng, in_time, out_lat, out_lng):
    """Converts inputted time at inputted longitude and latitude coordinates into concurrent time at output
    longitude and latitude coordinates.
    """
    timezone_in = get_timezone(in_lat, in_lng)
    time_in_with_timezone = get_timezone_and_time(in_time, timezone_in)
    timezone_out = get_timezone(out_lat, out_lng)
    converted_time = convert_to_timezone(time_in_with_timezone, timezone_out)
    return HttpResponse(converted_time)