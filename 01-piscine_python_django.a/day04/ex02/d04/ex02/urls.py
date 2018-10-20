from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^name$', views.get_name, name='name'),
    #url(r'^$', views.base, name='base'),
    url(r'^$', views.index, name='index'),
]
