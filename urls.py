from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponsePermanentRedirect

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', lambda request: HttpResponsePermanentRedirect('/images/')),

    # Images.
    ('^images/', include('images.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.STATIC_MEDIA_SERVER:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': 'media'}),
    )
