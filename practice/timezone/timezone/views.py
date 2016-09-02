"""timezone Views."""

from django.http import HttpResponse
from . import logic
import arrow


def get_server_time(request):
    """Retrieves the current time in UTC 8601 format."""
    current_time = logic.get_current_time().isoformat()
    return HttpResponse(current_time)


def get_timezone_at_lat_lng(request, lat, lng):
    """Retrieves the timezone name at inputted longitude and latitude coordinates.

    >>> test = get_timezone_at_lat_lng('request', '43.068888', '-121.008911')
    >>> test.content
    b'America/Los_Angeles'
    >>> test = get_timezone_at_lat_lng('request', '1', '1')
    >>> test.status_code
    404
    """
    try:
        lat, lng = float(lat), float(lng)
    except TypeError:
        return HttpResponse('Invalid input type. Please use numbers.', status=400)
    try:
        timezone = logic.get_timezone(lat, lng)
    except ValueError:
        return HttpResponse('Invalid coordinates', status=404)
    return HttpResponse(timezone)


def get_time_at_lat_lng(request, lat, lng):
    """Retrives the current time at inputted longitude and latitude coordinates.

    >>> test = get_time_at_lat_lng('request', '1', '1')
    >>> test.status_code
    400
    """
    try:
        lat, lng = float(lat), float(lng)
    except TypeError:
        return HttpResponse('Invalid input type. Please use numbers.', status=400)
    try:
        timezone = logic.get_timezone(lat, lng)
    except ValueError:
        return HttpResponse('Invalid coordinates', status=404)
    time_at_timezone = logic.get_time_at_timezone(timezone).isoformat()
    return HttpResponse(time_at_timezone)


def convert_time_from_lat_lngs(request, in_time, out_lat, out_lng):
    """Converts inputted time into concurrent time at output longitude and latitude coordinates.

    >>> test = convert_time_from_lat_lngs('request', '2013-05-09T03:59:59.999999-04:00', '43.068888', '-121.008911')
    >>> test.content
    b'2013-05-09T00:59:59.999999-07:00'
    >>> test = convert_time_from_lat_lngs('request', '2013-05-09T03:59:59.999999-04:00', '1', '1')
    >>> test.status_code
    400
    """
    try:
        out_lat, out_lng = float(out_lat), float(out_lng)
    except TypeError:
        return HttpResponse('Invalid input type. Please use numbers.', status=400)
    try:
        timezone_out = logic.get_timezone(out_lat, out_lng)
    except ValueError:
        return HttpResponse('Invalid coordinates', status=404)
    try:
        time_in = arrow.get(in_time)
    except arrow.parser.ParserError:
        return HttpResponse('Invalid time', status=400)
    converted_time = time_in.to(timezone_out)
    return HttpResponse(converted_time)

