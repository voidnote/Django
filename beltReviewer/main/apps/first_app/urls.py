from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^process/(?P<route>\w+)$', views.process, name = "process"),
    url(r'^logout$', views.logout, name = "logout"),
]


