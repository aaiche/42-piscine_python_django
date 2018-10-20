from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    #url(r'^init$', views.init),
    url(r'^init$', views.ex04_home),
    url(r'^populate$', views.ex04_populate),
    url(r'^display$', views.ex04_display),
    url(r'^remove$', views.ex04_remove),
]
    #url(r'^ex00$', login, {'template_name':'ex00/login.html' }),
