from django.contrib import admin
from django.urls import path,include
import features
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('schedule/', views.schedule, name='schedule'),
    path('gettinfo/', views.gettinfo, name='gettinfo'),
    path('gettrains/', views.gettrains, name='gettrains'),
    path('cancel/', views.cancel, name='cancel'),
    path('pnr/', views.pnr, name="pnr"),
    path('addT/', views.addT, name='addT'),
    path('addST/',views.addST, name='addST'),
    path('addR/', views.addR, name="addR"),
    path('addRT/', views.addRT, name='addRT'),



    ]