from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookprojecta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^book/', include('book.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
            # user auth urls
    url(r'^sign_in/$', 'bookprojecta.views.login'),
    url(r'^auth/$', 'bookprojecta.views.auth_view'),
    url(r'^logout/$', 'bookprojecta.views.logout'),
    url(r'^loggedin/$', 'bookprojecta.views.loggedin'),
    url(r'^invalid/$', 'bookprojecta.views.invalid_login'),
    url(r'^sign_up/$', 'bookprojecta.views.register_user'),
    url(r'^sign_up_success/$', 'bookprojecta.views.register_success'),
    url(r'^about/$', 'bookprojecta.views.about'),
    url(r'^contact/$', 'bookprojecta.views.contact'),



)
