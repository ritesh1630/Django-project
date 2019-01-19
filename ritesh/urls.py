from django.contrib import admin
from django.urls import path
from . import views
import ritesh
urlpatterns = [
    path('home',views.home),
    path('java',views.java),
    path('python',views.python),
    path('record', views.record),
    path('display',views.Custforms),
    path('emp',views.Empforms),
    path('sign', views.Sign_Up_View),


]