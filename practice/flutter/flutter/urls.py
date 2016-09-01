"""flutter URL Configuration

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
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name="index"),
    url(r'^post/submit$', views.render_post_ack, name="post_ack"),
    url(r'^post$', views.render_post_form, name="post_form"),
    url(r'^search$', views.render_search, name="search"),
    url(r'^login/ack$', views.render_login_ack, name="login_ack"),
    url(r'^login$', views.render_login, name="login"),
    url(r'^logout$', views.render_logout, name="logout"),
    url(r'^user/$', views.search_for_user_id, name="search_userid"),
    url(r'^user/(?P<user_id>.+)$', views.render_flutts_by_userid, name="flutts_by_userid")
]
