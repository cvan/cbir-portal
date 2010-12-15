from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'direct_to_template', {'template': 'index.html'}, name='index'),

    # Images.
    ('^images/', include('images.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.STATIC_MEDIA_SERVER:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': 'media'}),
    )
