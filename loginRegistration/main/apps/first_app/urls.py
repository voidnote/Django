from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/(?P<route>\w+)$', views.process),
    url(r'^success/(?P<id>\d+)/(?P<route>\w+)$', views.success),
]
