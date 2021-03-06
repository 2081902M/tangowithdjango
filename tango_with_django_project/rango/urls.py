__author__ = '2081902M'
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'about/', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'search/', views.search, name='search'),
        url(r'^goto/$', views.track_url, name='goto'),
        url(r'add_profile/', views.register_profile, name='add_profile'),
        url(r'profile/', views.profile, name='profile'),
        )
