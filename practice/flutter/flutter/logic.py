"""flutter Logic."""

from . import models
from django.contrib.auth import authenticate, login
import datetime


def create_and_save_flutt(user, body):
    """Creates a new Flutt object and saves to the database."""
    if not body:
        raise ValueError('Empty body')
    else:
        time = datetime.datetime.now()
        new_flutt = models.Flutt(author=user.username, body=body, timestamp=time, authorid=user.id)
        new_flutt.save()


def get_all_flutts():
    """Returns all posted Flutts"""
    return models.Flutt.objects.all()


def get_last_ten_flutts(flutts_list):
    """Takes a list of Flutts, returns the ten most recent Flutts sorted by most recent.

    >>> get_last_ten_flutts([models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34),\
    author_id=0), models.Flutt(author='Bob', body='1', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 35), author_id=1\
    )])
    [Flutt(author='Bob', body='1', timestamp=2016-09-02 10:28:35, author_id=1), Flutt(author='Fred', body='2', timestam\
p=2016-09-02 10:28:34, author_id=0)]
    """
    flutts_list_sorted = sorted(flutts_list, key=lambda Flutt: Flutt.timestamp, reverse=True)
    return flutts_list_sorted[:10]


def get_matches_by_search_text(search_text):
    """Takes a search text, searches through all posted Flutts for Flutts that contain that text, returns a list of
    Flutts that match.
    """
    matches = models.Flutt.objects.filter(body__contains=search_text)
    if not matches:
        raise LookupError('No matches')
    else:
        return matches


def login_user(request, username, password):
    """Logs the user in.

    Returns a ValueError if the login was unsuccessful, either because the user does not exist or the password was
    incorrect.
    """
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        raise ValueError('Invalid Login')


def get_username_display(username):
    """Takes in the user object tied to the request.

    If the user is logged in, returns a string which notifies user of what they are logged in as.

    If the user is not logged in, returns a string which notifies user that they are not logged in.

    >>> get_username_display('goofus')
    'You are currently logged in as goofus'
    >>> get_username_display('')
    'You are currently not logged in. Please login to add a Flutt.'
    """
    if username != '':
        return "You are currently logged in as " + username
    else:
        return "You are currently not logged in. Please login to add a Flutt."


def get_user_id(username):
    """Takes in a username, searches for a Flutt whose author corresponds to that username, then returns the author_id
    property of the Flutt, which is the user_id of that username.
    """
    try:
        flutt = models.Flutt.objects.filter(author=username)
        return flutt[0].author_id
    except IndexError:
        raise LookupError('No Flutts by that username')


def render_search_by_user_id(user_id):
    """Takes an author id, searches for all Flutts which have that author id."""
    return models.Flutt.objects.filter(author_id=user_id)
