from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/(?P<route>\w+)$', views.process),
    url(r'^secrets/(?P<id>\d+)/(?P<route>\w+)$', views.secrets),
    url(r'^share/(?P<id>\d+)$', views.post),
    url(r'^like/(?P<userid>\d+)/(?P<secretid>\d+)$', views.like),
    url(r'^logout$', views.logout),
]
