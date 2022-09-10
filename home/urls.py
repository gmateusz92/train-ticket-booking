from django.urls import path
from . import views
from django.urls import path,include
import features

urlpatterns = [
    path('', views.home, name="home"),


    ]