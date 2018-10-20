from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    #url(r'^init$', views.init),
    url(r'^models$', views.ex01_home),
]
    #url(r'^ex00$', login, {'template_name':'ex00/login.html' }),
