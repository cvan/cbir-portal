from django.conf.urls.defaults import patterns, url, include
from django.shortcuts import redirect

from . import views


urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url(r'^(?P<filename>.+)/similar$', views.similar, name='images.similar'),
    url(r'^(?P<filename>.+)/pgm-results$', views.pgm_results, name='images.pgm-results'),
)
