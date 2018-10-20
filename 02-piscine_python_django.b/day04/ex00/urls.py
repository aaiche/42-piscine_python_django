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
    url('^$', views.myEx00WithTemplate),


]


"""
^$: tous les motifs chaines vides
"""
