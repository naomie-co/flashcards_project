from django.urls import path
#from django.conf.urls import 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<slug:package>', views.create, kwargs={'package': None}, name='create'),
    path('package/', views.package, name='package'),
    ]