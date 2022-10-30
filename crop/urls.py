from os import name
from django.urls import path
from .views import *
from . import views

app_name = "crop"

urlpatterns = [
    path('',views.index,name='home'),
    path('crop/',views.crop,name='crop'),
    path('predict/',views.predict,name='predict')
]