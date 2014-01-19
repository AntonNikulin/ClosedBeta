from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                        url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "registration/login.html"}),
                        url(r"^logout/$", "django.contrib.auth.views.logout", {"next_page": "/"}),
                        url(r"^register/$", "ClosedBeta.views.registrationPage", name="registration"),
                        url(r"^",include("Games.urls")),
    # Examples:
    # url(r'^$', 'ClosedBeta.views.home', name='home'),
    # url(r'^ClosedBeta/', include('ClosedBeta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
