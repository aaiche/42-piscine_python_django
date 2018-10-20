from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^init$', views.ex02_init),
    url(r'^populate$', views.ex02_populate),
    url(r'^display$', views.ex02_display),
]
