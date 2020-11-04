from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name="home"),
    path('getinfo',views.getinfo,name='getinfo')
]