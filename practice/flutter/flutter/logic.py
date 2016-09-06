"""flutter Logic."""

from . import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import datetime
from django.test import client
from django.contrib.auth import logout


def create_and_save_flutt(username, body, time, user_id):
    """Creates a new Flutt object and saves to the database.

    >>> create_and_save_flutt('adkinsbass', 'Radical!', datetime.datetime(2016, 9, 2, 10, 28, 34), 0)
    >>> models.Flutt.objects.get(author='adkinsbass', body='Radical!')
    Flutt(author='adkinsbass', body='Radical!', timestamp=2016-09-02 10:28:34+00:00, author_id=0)
    """
    if not body:
        raise ValueError('Empty body')
    else:
        new_flutt = models.Flutt(author=username, body=body, timestamp=time, author_id=user_id)
        new_flutt.save()


def get_current_time():
    """Returns the server time at moment of access."""
    return datetime.datetime.now()


def get_all_flutts():
    """Returns all posted Flutts.

    >>> models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34), author_id=0).save()
    >>> list(get_all_flutts())
    [Flutt(author='Fred', body='2', timestamp=2016-09-02 10:28:34+00:00, author_id=0)]
    """
    return models.Flutt.objects.all()


def sort_flutts_by_most_recent(flutts_list):
    """Takes a list of Flutts, returns them sorted by most recent.

    >>> sort_flutts_by_most_recent([models.Flutt(author='Fred', body='2', timestamp=datetime.datetime\
    (2016, 9, 2, 10, 28, 34), author_id=0), models.Flutt(author='Bob', body='1', timestamp=datetime.datetime\
    (2016, 9, 2, 10, 28, 35), author_id=1)])
    [Flutt(author='Bob', body='1', timestamp=2016-09-02 10:28:35, author_id=1), Flutt(author='Fred', body='2', timestam\
p=2016-09-02 10:28:34, author_id=0)]
    """
    return sorted(flutts_list, key=lambda Flutt: Flutt.timestamp, reverse=True)


def get_matches_by_search_text(search_text):
    """Takes a search text, searches through all posted Flutts for Flutts that contain that text, returns a list of
    Flutts that match.

    >>> models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34), author_id=0).save()
    >>> get_matches_by_search_text(2)
    <QuerySet [Flutt(author='Fred', body='2', timestamp=2016-09-02 10:28:34+00:00, author_id=0)]>
    >>> get_matches_by_search_text(3)
    Traceback (most recent call last):
    ...
    LookupError: No matches
    """
    matches = models.Flutt.objects.filter(body__contains=search_text)
    if not matches:
        raise LookupError('No matches')
    else:
        return matches


def login_user(request, username, password):
    """Logs the user in.

    Returns a LookupError if the username does not exist.

    Returns a ValueError if the password was incorrect.

    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> c = client.Client()
    >>> c.login(username='john', password='johnpassword')
    True
    >>> login_user('request', 'john', 'floorb')
    Traceback (most recent call last):
    ...
    ValueError: Incorrect password
    >>> login_user('request', 'fee', 'foo')
    Traceback (most recent call last):
    ...
    LookupError: That user does not exist.
    """
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        raise LookupError('That user does not exist.')
    else:
        raise ValueError('Incorrect password')


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
    """Takes in a username, returns the user id for the user who has that username.

    If there is no user with that username, raises a LookupError.
    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> user.save()
    >>> get_user_id('john')
    1
    >>> get_user_id('food')
    Traceback (most recent call last):
    ...
    LookupError: That user does not exist

    """
    try:
        user = User.objects.get(username=username)
        return user.id
    except User.DoesNotExist:
        raise LookupError('That user does not exist')


def search_by_user_id(user_id):
    """Takes an author id, searches for all Flutts which have that author id.

    If there are no Flutts by that user, raises a LookupError.

    >>> models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34), author_id=0).save()
    >>> search_by_user_id(0)
    <QuerySet [Flutt(author='Fred', body='2', timestamp=2016-09-02 10:28:34+00:00, author_id=0)]>
    """
    matches = models.Flutt.objects.filter(author_id=user_id)
    if not matches:
        raise LookupError('No Flutts for this user.')
    else:
        return matches

def logout_user(request):
    """Logs out the current logged in user.

    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> c = client.Client()
    >>> login = c.login(username='john', password='johnpassword')
    >>> response = c.get('/logout')
    >>> 'user' in response.request.keys()
    False
    """
    logout(request)
    return request
