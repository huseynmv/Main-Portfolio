from django.urls import path
from . views import main

app_name = 'portfolio'

urlpatterns = [
    path('', main, name='index'),
]