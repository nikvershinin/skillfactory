from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('aboutme/', aboutme, name='aboutme'),
]