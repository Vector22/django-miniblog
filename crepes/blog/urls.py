from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('article/<slug:slug>', views.lire_article, name='blog_lire'),
]
