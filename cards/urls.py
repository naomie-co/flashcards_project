from django.urls import path, include
from django.contrib.auth import views as auth_views
#from django.conf.urls import 
from . import views

app_name = 'cards'
urlpatterns = [
    #path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('learn/<str:package>', views.learn, name='learn'),
    path('learning_stat/', views.learning_stat, name='learning_stat'),
    ]