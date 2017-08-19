from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^tracks/$', views.tracks_list, name='tracks_list'),
    url(r'^genres/$', views.genres_list, name='genres_list'),
    url(r'^tracks/(?P<pk>\d+)/$', views.tracks_detail, name='tracks_detail'),
    url(r'^genres/(?P<pk>\d+)/$', views.genre_detail, name='genre_detail'),
    url(r'^new$', views.new, name='new'),
    url(r'new_track/$', views.new_track, name='new_track'),
    url(r'new_genre/$', views.new_genre, name='new_genre'),
    url(r'^tracks/(?P<pk>\d+)/edit/$', views.track_edit, name='track_edit'),
    url(r'^genres/(?P<pk>\d+)/edit/$', views.genre_edit, name='genre_edit'),
    url(r'search_track/$', views.search_track, name='search_track'),
    url(r'search_genre/$', views.search_genre, name='search_genre'),
]
