"""multimadlib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.render_index, name='index'),
    url(r'^new/ack$', views.render_new_madlib_ack, name='new_madlib_ack'),
    url(r'^new$', views.render_new_madlib, name='new_madlib'),
    url(r'^madlib/(?P<madlib_name>.+)/form$', views.render_madlib_form, name='madlib_form'),
    url(r'^madlib/(?P<madlib_name>.+)$', views.render_madlib_display, name='madlib_display')

]
