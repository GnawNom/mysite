from django.conf.urls.defaults import patterns, include, url
from views import hello, current_datetime, hours_ahead, header
from django.contrib import admin
from mysite.books import views
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    (r'^header/$', header),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),

	
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
