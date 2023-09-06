from os import name

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from travelapp import views
from travelproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.demo,name='demo')
    ]

