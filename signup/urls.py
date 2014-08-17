from django.conf.urls import patterns, include, url
from signup.views import SignupPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', SignupPage.as_view(), name='signup_page'),
                       )
