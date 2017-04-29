from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "mainpage"),
    url(r'^newreview$', views.add_review, name = "add_review"),
    url(r'^createreview$', views.create_review, name = "create_review"),
    url(r'^showreview$', views.show_review, name = "show_review"),
]

