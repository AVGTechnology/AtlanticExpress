from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [

    path("", views.index, name='index'),
    path("track_id/", views.track_id, name='track_id'),

]
