from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    #url(r'^init$', views.init),
    url(r'^init$', views.ex02_home),
    url(r'^populate$', views.ex02_populate),
    url(r'^display$', views.ex02_display),
]
    #url(r'^ex00$', login, {'template_name':'ex00/login.html' }),
