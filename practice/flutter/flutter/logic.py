"""flutter Logic."""

from . import models
from django.contrib.auth.models import User
import datetime
from operator import attrgetter


def create_and_save_flutt(username, body, time, user_id):
    """Creates a new Flutt object and saves to the database.

    >>> create_and_save_flutt('adkinsbass', 'Radical!', datetime.datetime(2016, 9, 2, 10, 28, 34), 0)
    >>> models.Flutt.objects.get(author='adkinsbass', body='Radical!')
    Flutt(author='adkinsbass', body='Radical!', timestamp=2016-09-02 10:28:34+00:00, author_id=0)
    """
    if len(body) < 1:
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
    return sorted(flutts_list, key=attrgetter('timestamp'), reverse=True)


def get_matches_by_search_text(search_text):
    """Takes a search text, searches through all posted Flutts for Flutts that contain that text, returns a list of
    Flutts that match.

    >>> models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34), author_id=0).save()
    >>> get_matches_by_search_text(2)
    <QuerySet [Flutt(author='Fred', body='2', timestamp=2016-09-02 10:28:34+00:00, author_id=0)]>
    """
    return models.Flutt.objects.filter(body__contains=search_text)


def get_user(username):
    """Takes in a username, returns the user object of that username.

    If there is no user with that username, raises a LookupError.
    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> user.save()
    >>> get_user('john')
    <User: john>
    >>> get_user('food')
    Traceback (most recent call last):
    ...
    LookupError: That user does not exist

    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        raise LookupError('That user does not exist')


def search_by_user_id(user_id):
    """Takes an author id, searches for all Flutts which have that author id.

    >>> models.Flutt(author='Fred', body='2', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 34), author_id=0).save()
    >>> search_by_user_id(0)
    <QuerySet [Flutt(author='Fred', body='2', timestamp=2016-09-02 10:28:34+00:00, author_id=0)]>
    """
    return models.Flutt.objects.filter(author_id=user_id)
