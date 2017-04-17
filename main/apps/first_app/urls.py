from django.conf.urls import url
from . import views           # This gives us access to everything (.) in a views.py file that Django automatically created for us when we built our first_app. 
urlpatterns = [
    url(r'^$', views.index)   
]