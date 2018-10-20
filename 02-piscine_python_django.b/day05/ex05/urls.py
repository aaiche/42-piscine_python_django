from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^readme$', views.ex05_readme),
    url(r'^populate$', views.ex05_populate),
    url(r'^display$', views.ex05_display),
    url(r'^remove$', views.ex05_remove),
]
