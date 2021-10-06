from django.urls import path
#from django.conf.urls import 
from . import views

urlpatterns = [
    path(' ', views.index, name='index'),
    path('create/<slug:package>', views.create, name='create'),
    path('package/<slug:package>', views.package, name='package'),
    ]