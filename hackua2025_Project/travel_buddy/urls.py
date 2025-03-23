
from django.urls import path
from .views import *

urlpatterns = [
    path('mood/', mood, name='mood')
]
