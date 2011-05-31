from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/chatapp1'}, name='home.default'),
    url(r'chatapp1', include('chatapp1.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # socket.io endpoint
    url(r'^socket\.io', 'chatapp1.views.socketio', name='chatapp1.socketio')
)

urlpatterns += staticfiles_urlpatterns()
