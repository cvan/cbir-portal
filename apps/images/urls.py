from django.conf.urls.defaults import patterns, url, include
from django.shortcuts import redirect

from . import views

urlpatterns = patterns('',
    url('^$', views.home, name='home'),
'''
    url(r'^upload/image/(?P<model_name>\w+\.\w+)/(?P<object_pk>\d+)$',
        'up_image_async', name='upload.up_image_async'),
    url(r'^upload/image/delete/(?P<image_id>\d+)$',
        'del_image_async', name='upload.del_image_async'),
'''
)
