from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.helloworld, name='helloworld'),
  url(r'^list/$', views.list, name='list'),
  url(r'^create/$', views.create, name='create'),
  url(r'^save/$', views.save, name='save'),
  url(r'^modify/$', views.modify, name='modify'),
  url(r'^delete/$', views.delete, name='delete'),
  url(r'^login/$', views.userlogin, name='userlogin'),
  url(r'^logout/$', views.userlogout, name='userlogout'),
]

