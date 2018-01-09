from django.conf.urls import url, include
from django.contrib import admin
from .views import MainView, StatsView


urlpatterns = [
    url(r'^$', MainView.index, name='index'),
    url(r'^upload/$', StatsView.upload, name='upload'),
]