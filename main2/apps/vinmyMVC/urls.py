from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show),
    url(r'^new_user$', views.create),
    url(r'^time$', views.time),
    url(r'^random$', views.randomword)
]
