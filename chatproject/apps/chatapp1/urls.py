from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('chatapp1.views',
    url(r'^$', 'chat', name='chatapp1'),
)
