from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', view=views.dashboard, name='dashboard'),
    url(r'^login$', view=views.logindialog, name='login'),
    url(r'^profile',view=views.userprofile,name='profile')

]
