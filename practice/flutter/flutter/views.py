"""flutter Views."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.test import RequestFactory
from django.contrib.sessions.backends.db import SessionStore
from . import logic


def render_index(request):
    """View for rendering index without any search terms."""
    all_flutts = logic.get_all_flutts()
    sorted_flutts_all = logic.sort_flutts_by_most_recent(all_flutts)
    arguments = {
        'last_ten_flutts': sorted_flutts_all[:10],
        'username': request.user.username
    }
    return render(request, 'flutter/index.html', arguments)


@login_required(login_url="login")
def render_post_form(request):
    """Renders the form for posting a Flutt.

    Requires login by the user, will direct someone who is not logged in to login page.
    """
    arguments = {
        'username': request.user.username
    }
    return render(request, 'flutter/post_form.html', arguments)


def render_post_ack(request):
    """Receives Flutt data, creates flutt and saves, and acknowledges receipt.

    Returns a 400 response if the user did not add something to the body of the Flutt.
    """
    username = request.user.username
    body = request.POST['body']
    time = logic.get_current_time()
    user_id = request.user.id
    try:
        logic.create_and_save_flutt(username, body, time, user_id)
    except ValueError:
        return HttpResponse('You forgot to write something! <a href="/post">Please try again</a>', status=400)
    arguments = {
        'username': username
    }
    return render(request, 'flutter/post_ack.html', arguments)


def render_search(request):
    """Detects what kind of search the user is attempting (by user or by text).

    If it is by user, gets the user ID of the searched user, then directs to the 'search_by_user_id' url. If there is no
    user by that name, or if they haven't posted a Flutt, returns a 400 response.

    If it is by text, completes the search and returns 10 matches sorted by most recent. If there are no results,
    returns a 400 response.
    """
    if 'searchtext' in request.GET:
        search_text = request.GET.get('searchtext', False)
        matches = logic.get_matches_by_search_text(search_text)
        sorted_flutts_by_search_text = logic.sort_flutts_by_most_recent(matches)
        arguments = {
            'last_ten_flutts': sorted_flutts_by_search_text[:10],
            'username': request.user.username
        }
        return render(request, 'flutter/index.html', arguments)
    elif 'searchuser' in request.GET:
        username = request.GET['searchuser']
        try:
            user = logic.get_user(username)
        except LookupError:
            return HttpResponse('Sorry, that user doesn\'t exist. <a href="/">Please try again.</a>', status=400)
        return HttpResponseRedirect('user/' + str(user.id))


def render_search_by_userid(request, user_id):
    """Searches for all flutts by inputted user, returns 10 matches sorted by most recent."""
    try:
        flutts_by_user_id = logic.search_by_user_id(user_id)
    except LookupError:
        return HttpResponse('Sorry, that user has not posted a Flutt. <a href="/">Please try again.</a>', status=400)
    sorted_flutts_by_user_id = logic.sort_flutts_by_most_recent(flutts_by_user_id)
    arguments = {
        'last_ten_flutts': sorted_flutts_by_user_id[:10],
        'username': request.user.username
    }
    return render(request, 'flutter/index.html', arguments)


def render_login(request):
    """Renders the login page."""
    return render(request, 'flutter/login.html')


def render_login_ack(request):
    """Logs the user in, and returns an acknowledgment on successful login.

    If the password was incorrect or the username does not exist, returns a 400 response.

    >>> factory = RequestFactory()
    >>> request = factory.post('/login/ack', {'username': 'john', 'password': 'johnpassword'})
    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> session = SessionStore()
    >>> session.create()
    >>> request.session = session
    >>> response = render_login_ack(request)
    >>> response.status_code
    200
    >>> factory = RequestFactory()
    >>> request = factory.post('/login/ack', {'username': 'john', 'password': 'floorb'})
    >>> response = render_login_ack(request)
    >>> response.status_code
    400
    >>> factory = RequestFactory()
    >>> request = factory.post('/login/ack', {'username': 'dfe', 'password': 'johnpassword'})
    >>> response = render_login_ack(request)
    >>> response.status_code
    400

    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse('Invalid login. <a href="/login">Please try again.</a>', status=400)
        login(request, user)
    else:
        return HttpResponse('Invalid login. <a href="/login">Please try again.</a>', status=400)
    arguments = {
        'success': 'Successful login!'
    }
    return render(request, 'flutter/login_ack.html', arguments)


def render_logout(request):
    """Logs the user out.

    >>> factory = RequestFactory()
    >>> request = factory.get('/logout')
    >>> request.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> session = SessionStore()
    >>> session.create()
    >>> request.session = session
    >>> response = render_logout(request)
    >>> isinstance(request.user, AnonymousUser)
    True
    """
    logout(request)
    return render(request, 'flutter/logout_ack.html')
