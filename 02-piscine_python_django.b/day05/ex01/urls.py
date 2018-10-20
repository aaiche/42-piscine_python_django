from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^models$', views.ex01_home),
]
