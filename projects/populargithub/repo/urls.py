from django.conf.urls import patterns, url

from repo import views

urlpatterns = patterns('',
    url(r'^$', views.populate, name='populate'),
)