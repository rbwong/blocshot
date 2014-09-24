from django.conf.urls import patterns, include, url
from signup.views import SignupPage, IndexView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='home_page'),
                       (r'^channel/', TemplateView.as_view(template_name="channel.html")),
                       )
