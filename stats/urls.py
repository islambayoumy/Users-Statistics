from django.conf.urls import url, include
from django.contrib import admin
from .views import MainView, CsvView


urlpatterns = [
    url(r'^$', MainView.index, name='index'),
    url(r'^upload/$', CsvView.upload, name='upload'),
]