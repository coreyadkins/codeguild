"""flutter Views."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import logic


def render_index(request):
    """View for rendering index without any search terms."""
    all_flutts = logic.get_all_flutts()
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'last_ten_flutts': logic.get_last_ten_flutts(all_flutts),
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
    user = request.user
    body = request.POST['body']
    try:
        logic.create_and_save_flutt(user, body)
    except ValueError:
        return HttpResponse('You forgot to write something! Please try again', status=400)
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'username_display': username_display
    }
    return render(request, 'flutter/post_ack.html', arguments)


def render_search(request):
    """Detects what kind of search the user is attempting (by user or by text).

    If it is by user, gets the user ID of the searched user, then directs to the 'search_by_user_id' url.

    If it is by text, completes the search and returns 10 matches sorted by most recent.

    If both fields have values, returns a 400 response directing user to only fill in one field per search.
    """
    if request.GET.get('searchuser', False) != '' and request.GET.get('searchtext', False) != '':
        return HttpResponse('Please enter only one field per search.', status=400)
    elif request.GET.get('searchuser', False) != '':
        username = request.GET['searchuser']
        try:
            user_id = logic.get_user_id(username)
        except IndexError:
            return HttpResponse('Sorry, either that user doesn\'t exist, or they haven\'t posted a Flutt. Try another',
                                status=400)
        return HttpResponseRedirect('user/' + str(user_id))
    else:
        search_text = request.GET.get('searchtext', False)
        matches = logic.get_matches_by_search_text(search_text)
        username_display = logic.get_username_display(request.user.username)
        arguments = {
            'last_ten_flutts': logic.get_last_ten_flutts(matches),
            'username_display': username_display
        }
        return render(request, 'flutter/index.html', arguments)


def render_search_by_userid(request, user_id):
    """Searches for all flutts by inputted user, returns 10 matches sorted by most recent."""
    flutts_by_user = logic.render_search_by_user_id(user_id)
    username_display = logic.get_username_display(request.user.username)
    arguments = {
        'last_ten_flutts': logic.get_last_ten_flutts(flutts_by_user),
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)


def render_login(request):
    """Renders the login page."""
    return render(request, 'flutter/login.html')


def render_login_ack(request):
    """Logs the user in, and returns an acknowledgment on successful login.

    If the login is not valid, returns a 400 response."""
    username = request.POST['username']
    password = request.POST['password']
    try:
        logic.login_user(request, username, password)
    except ValueError:
        return HttpResponse('Invalid login', status=400)
    arguments = {
        'success': 'Successful login!'
    }
    return render(request, 'flutter/login_ack.html', arguments)


def render_logout(request):
    """Logs the user out."""
    logout(request)
    return render(request, 'flutter/logout_ack.html')
