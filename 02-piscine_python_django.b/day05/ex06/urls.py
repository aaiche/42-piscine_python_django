from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^init$', views.ex06_home),
    url(r'^populate$', views.ex06_populate),
    url(r'^display$', views.ex06_display),
    url(r'^update$', views.ex06_update),
]
