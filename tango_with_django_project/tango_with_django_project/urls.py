from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import password_change, password_change_done
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/add_profile/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^/accounts/password/change/done/$', 'django.contrib.auth.views.password_change_done', {'password_change_complete': 'rango/password_change.html'}),
    (r'^/accounts/password/change/$', 'django.contrib.auth.views.password_change', {'password_change': 'rango/password_change.html'})
    #(r'^accounts/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
