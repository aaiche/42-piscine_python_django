#from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name="init"),
    path('worldmap/', views.worldmap, name="worldmap"),
    path('options/load/', views.load, name="load"),
    path('options/load_A/', views.load_A, name="load_A"),
    path('options/load_up/', views.load_up, name="load_up"),
    path('options/load_down/', views.load_down, name="load_down"),
    path('options/save_game/', views.save, name="save"),
    path('options/save_A/', views.save_A, name="save_A"),
    path('options/save_B', views.save_B, name="save_B"),
    path('options/save_up/', views.save_up, name="save_up"),
    path('options/save_down/', views.save_down, name="save_down"),
    path('up/', views.up, name="up"),
    path('down/', views.down, name="down"),
    path('left/', views.left, name="left"),
    path('right/', views.right, name="right"),
    path('options/', views.options, name="options"),
    path('moviedex/', views.moviedex, name="moviedex"),
    path('moviedex_up/', views.moviedex_up, name="moviedex_up"),
    path('moviedex_down/', views.moviedex_down, name="moviedex_down"),
    path('moviedex/<str:moviemon>/', views.details, name="details"),
    path('battle/<str:moviemon>/', views.battle, name="battle"),
    path('battle_A/<str:moviemon>/', views.battle_A, name="battle_A"),
]
