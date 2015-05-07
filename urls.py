from django.conf.urls import *
from django.views.generic import TemplateView

 
urlpatterns = patterns('',
    (r'^/(?P<section_url>[a-zA-Z0-9_.-]+)/(?P<storytitle>[a-zA-Z0-9_.-]+)', 'bigstory.views.Storypage'),
    (r'^', 'bigstory.views.Main'),
)
