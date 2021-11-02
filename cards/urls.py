from django.urls import path
#from django.conf.urls import 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('learn/<str:package>', views.learn, name='learn'),
#    path('package/', views.package, name='package'),
    ]