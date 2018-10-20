from django.conf.urls import url
from . import views
#    url('^$', views.myEx00),
#     url('template', views.myEx00WithTemplate),
"""
    url('base', views.base),
    url('inherit', views.inherit),
    url('context', views.context_example),
    url('forrr', views.for_eample),
    url('if', views.if_eample),
    url('include', views.include_example),
    url('formm', views.withform),
"""
urlpatterns = [
    url(r'^$', views.day05_home),
    url(r'^init$', views.ex00_home),


]
#    url('init', views.create_table),


"""
^$: tous les motifs chaines vides
"""
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day05_home),
    #url(r'^init$', views.init),
    url(r'^init$', views.ex00_home),
]
"""
    #url(r'^ex00$', login, {'template_name':'ex00/login.html' }),
