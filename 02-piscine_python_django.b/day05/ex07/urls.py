from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^readme$', views.ex07_readme),
    url(r'^populate$', views.ex07_populate),
    url(r'^display$', views.ex07_display),
    url(r'^update$', views.ex07_update),
]
