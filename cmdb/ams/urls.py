# encoding:utf-8

from django.conf.urls import url
from .views import index, list,add, userlogin, userlogout, delete, update

urlpatterns = [
    url(r'^$', view=list, name="list"),
    url(r'^list/$', view=list, name="list"),
    url(r'^add/$', view=add, name="add"),
    url(r'^delete/(?P<pk>\d+)/$', view=delete, name="delete"),
    url(r'^update/(?P<pk>\d+)/$', view=update, name="update"),
    url(r'^userlogin/$', view=userlogin, name="userlogin"),
    url(r'^userlogout/$', view=userlogout, name="userlogout"),
]
