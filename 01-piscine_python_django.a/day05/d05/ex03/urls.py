from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    #url(r'^init$', views.init),
    url(r'^readme$', views.ex03_readme),
    url(r'^populate$', views.ex03_populate),
    url(r'^display$', views.ex03_display),
]
    #url(r'^ex00$', login, {'template_name':'ex00/login.html' }),
