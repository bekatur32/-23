from django.urls import path
from .views import ada

urlpatterns = [
    path('',ada,name='home')
]
