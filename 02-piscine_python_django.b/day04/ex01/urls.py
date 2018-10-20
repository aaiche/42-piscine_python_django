from django.conf.urls import url
from . import views

urlpatterns = [


    url('django', views.django),
    url('affichage', views.affichage),
    url('templates', views.templates),
]
