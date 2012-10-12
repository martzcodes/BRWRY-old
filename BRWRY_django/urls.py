from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BRWRY_django.views.home', name='home'),
    # url(r'^BRWRY_django/', include('BRWRY_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

#    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    (r'^$', 'BRWRY_bootstrap.views.BRWRY_index', {}, "home"),
    (r'^about$', direct_to_template, {'template': 'about.html'}, "about"),
    (r'^contact$', direct_to_template, {'template': 'contact.html'}, "contact"),
    (r'^form$', 'BRWRY_bootstrap.views.BRWRY_form'),
    (r'^configure$', 'BRWRY_bootstrap.views.BRWRY_configure'),
    (r'^form_template$', 'BRWRY_bootstrap.views.BRWRY_form_with_template'),
    (r'^form_inline$', 'BRWRY_bootstrap.views.BRWRY_form_inline'),
    (r'^tabs$', 'BRWRY_bootstrap.views.BRWRY_tabs', {}, "tabs"),
    (r'^widgets$', 'BRWRY_bootstrap.views.BRWRY_widgets', {}, "widgets"),
)
