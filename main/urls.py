from django.conf.urls.defaults import *
#import settings


urlpatterns = patterns('main.views',
    url(r'^see$', 'home', name='home'),
    url(r'^user/(?P<pk>\d+)$', 'show_user', name='show_user'),
    url(r'^user/edit$', 'edit_user', name='edit_user'),
    url(r'^user/(?P<pk>\d+)/delete$', 'delete_user', name='delete_user'),
    url(r'^user/add/$', 'add_user',name='add_user'),
    url(r'^edit/tweet/(?P<pk>\d+)$', 'edit_tweet', name='edit_tweet'),
    url(r'^tweet/(?P<pk>\d+)/delete$', 'delete_tweet', name='delete_tweet'),
    url(r'^tweet/add/$', 'add_tweet',name='add_tweet'),
    url(r'^follow/(?P<pk>\d+)$', 'show_follow',name='show_follow'),
    url(r'^add_tweet/$', 'add_tweet',name='add_tweet'),
    url(r'^tweet/delete/(?P<pk>\d+)$', 'delete_tweet', name='delete_tweet'),
#(r'^photo/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'index', name='index'),
    url(r'^following/$', 'following'),
    url(r'^accounts/login/$', 'login', name='login'),

)
