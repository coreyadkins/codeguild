"""flutter Views."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import logic


def render_index(request):
    all_flutts = logic.get_all_flutts()
    last_ten_flutts_all = logic.get_last_ten_flutts(all_flutts)
    username_display = logic.get_username_display(request)
    arguments = {
        'last_ten_flutts': last_ten_flutts_all,
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)


@login_required(login_url="login")
def render_post_form(request):
    username_display = logic.get_username_display(request)
    arguments = {
        'username_display': username_display
    }
    return render(request, 'flutter/post_form.html', arguments)


def render_post_ack(request):
    logic.authenticate_user(request)
    user = request.user
    body = request.POST['body']
    logic.create_and_save_flutt(user, body)
    username_display = logic.get_username_display(request)
    arguments = {
        'username_display': username_display
    }
    return render(request, 'flutter/post_ack.html', arguments)


def render_search(request):
    searchtext = request.GET['search']
    matches = logic.get_matches_by_search(search)
    last_ten_flutts_by_search = logic.get_last_ten_flutts(matches)
    username_display = logic.get_username_display(request)
    arguments = {
        'last_ten_flutts': last_ten_flutts_by_search,
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)


def render_login(request):
    return render(request, 'flutter/login.html')


def render_login_ack(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        logic.login_user(request, username, password)
    except ValueError:
        arguments = {
            'success': 'Invalid login'
        }
        return render(request, 'flutter/login_ack.html', arguments)
    arguments = {
        'success': 'Successful login!'
    }
    return render(request, 'flutter/login_ack.html', arguments)


def render_logout(request):
    logout(request)
    return render(request, 'flutter/logout_ack.html')

def search_for_user_id(request):
    username = request.GET['searchuser']
    user_id = logic.get_userid(username)
    HttpResponseRedirect('user/' + user_id)

def render_flutts_by_userid(request, user_id):
    flutts_by_user = logic.get_flutts_by_user(user_id)
    last_ten_flutts_for_user = logic.get_last_ten_flutts(flutts_by_user)
    username_display = logic.get_username_display(request)
    arguments = {
        'last_ten_flutts': last_ten_flutts_for_user,
        'username_display': username_display
    }
    return render(request, 'flutter/index.html', arguments)