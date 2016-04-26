from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'', include('registration.backends.simple.urls')),
    url(r'^player_history/(?P<player_id>[0-9]+)/$', \
            views.player_history, \
            name='player_history'),
    url(r'^weekly_recap/(?P<week_id>[0-9]+)/$', \
            views.weekly_recap, \
            name='weekly_recap'),
    url(r'^record_game/(?P<player_id>[0-9]+)/$', \
            views.record_game, \
            name='record_game')
]

