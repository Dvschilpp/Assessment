from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # define patterns to query for site navigation
    url(r'^$', 'mysite.views.index'),
	url(r'^/$', 'mysite.views.index'),
	url(r'^about$', 'mysite.views.about'),
    url(r'^admin/', include(admin.site.urls)),
)
