from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^affichage$', views.affichage, name='affichage'),
    url(r'^templates$', views.templates, name='templates'),
    url(r'^django$', views.django, name='django'),
    url(r'^$', views.base, name='base'),
    url(r'^$', views.index, name='index'),
]

