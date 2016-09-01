"""flutter Logic."""

from . import models
from django.contrib.auth import authenticate, login
import datetime

def create_and_save_flutt(user, body):
    time = datetime.datetime.now()
    new_flutt = models.Flutt(author=user, body=body, timestamp=time)
    new_flutt.save()


def get_all_flutts():
    return models.Flutt.objects.all()


def get_last_ten_flutts(flutts_list):
    flutts_list_sorted = sorted(flutts_list, key=lambda Flutt: Flutt.timestamp, reverse=True)
    return flutts_list_sorted[:10]


def get_matches_by_search(search):
    return models.Flutt.objects.filter(body__contains=search)


def login_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        raise ValueError('Invalid Login')


def get_username_display(request):
    user = request.user.username
    if user != '':
        return "You are currently logged in as " + user
    else:
        return "You are currently not logged in. Please login to add a Flutt."


def get_userid(username):
    flutt = models.Flutt.objects.get(username=username)
    return flutt.author.id


def get_flutts_by_user(user_id):
    return models.Flutt.objects.filter(username__id=user_id)
