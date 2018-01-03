# -*- coding: utf-8 -*-
# Import django modules
from django.conf.urls import url
from django.contrib import admin
from waypointsApp import views
# Import custom modules
import settings



admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='waypoints-index'),
    url(r'^save$', views.save, name='waypoints-save'),
    url(r'^search$', views.search, name='waypoints-search'),
    url(r'^upload$', views.upload, name='waypoints-upload'),
]