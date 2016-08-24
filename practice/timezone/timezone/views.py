"""timezone Views."""

from django.http import HttpResponse
from . logic import get_current_time, get_timezone, get_time_at_timezone


def get_server_time(request):
    current_time = get_current_time()
    return HttpResponse(current_time)

def get_timezone_at_lat_lng(request, lat, lng):
    timezone = get_timezone(lat, lng)
    return HttpResponse(timezone)

def get_time_at_lat_lng(request, lat, lng):
    timezone = get_timezone(lat, lng)
    time_at_timezone = get_time_at_timezone(timezone)
    return HttpResponse(time_at_timezone)

def convert_time_from_lat_lngs(request, in_lat, in_lng, in_time, out_lat, out_lng):
    timezone_in = get_timezone(in_lat, in_lng)
    timezone_out = get_timezone(out_lat, out_lng)
    
    return HttpResponse('hi')