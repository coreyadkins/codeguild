"""flutter Views."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import logic


def render_index(request):
    """View for rendering index without any search terms."""
    all_flutts = logic.get_all_flutts()
    sorted_flutts_all = logic.sort_flutts_by_most_recent(all_flutts)
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'last_ten_flutts': sorted_flutts_all[:10],
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)


@login_required(login_url="login")
def render_post_form(request):
    """Renders the form for posting a Flutt.

    Requires login by the user, will direct someone who is not logged in to login page.
    """
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'username_display': username_display
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
    username_display = logic.get_username_display(user.username)
    arguments = {
        'username_display': username_display
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
        try:
            matches = logic.get_matches_by_search_text(search_text)
        except LookupError:
            return HttpResponse('No results for that search text. <a href="/">Please try again.<a>', status=400)
        sorted_flutts_by_search_text = logic.sort_flutts_by_most_recent(matches)
        username_display = logic.get_username_display(request.user.username)
        arguments = {
            'last_ten_flutts': sorted_flutts_by_search_text[:10],
            'username_display': username_display
        }
        return render(request, 'flutter/index.html', arguments)
    elif 'searchuser' in request.GET:
        username = request.GET['searchuser']
        try:
            user_id = logic.get_user_id(username)
        except LookupError:
            return HttpResponse('Sorry, that user doesn\'t exist. <a href="/">Please try again.</a>', status=400)
        return HttpResponseRedirect('user/' + str(user_id))


def render_search_by_userid(request, user_id):
    """Searches for all flutts by inputted user, returns 10 matches sorted by most recent."""
    try:
        flutts_by_user_id = logic.search_by_user_id(user_id)
    except LookupError:
        return HttpResponse('Sorry, that user has not posted a Flutt. <a href="/">Please try again.</a>', status=400)
    sorted_flutts_by_user_id = logic.sort_flutts_by_most_recent(flutts_by_user_id)
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'last_ten_flutts': sorted_flutts_by_user_id[:10],
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)


def render_login(request):
    """Renders the login page."""
    return render(request, 'flutter/login.html')


def render_login_ack(request):
    """Logs the user in, and returns an acknowledgment on successful login.

    If the password was incorrect, returns a 400 response.

    If the username does not exist, returns a 404 response.
    """
    username = request.POST['username']
    password = request.POST['password']
    try:
        logic.login_user(request, username, password)
    except ValueError:
        return HttpResponse('Incorrect password. <a href="/login">Please try again.</a>', status=400)
    except LookupError:
        return HttpResponse('That username does not exist.', status=404)
    arguments = {
        'success': 'Successful login!'
    }
    return render(request, 'flutter/login_ack.html', arguments)


def render_logout(request):
    """Logs the user out."""
    logic.logout_user(request)
    return render(request, 'flutter/logout_ack.html')
