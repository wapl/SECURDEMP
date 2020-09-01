from django.urls import path 
from . import views

urlpatterns=[
     path('search/', views.SearchView, name='search_results'),
    path('', views.index, name='index'),
]