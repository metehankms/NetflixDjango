from django.urls import path
from .views import *


urlpatterns = [
    path('',anasayfa,name="anasayfa"),
    path('browse/',profiles,name="profiles"),
    path('browse_index/',browse_index,name="browse_index"),
    path('video/',video,name="video"),
    
]