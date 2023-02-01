from django.urls import path
from . import views


app_name = 'sobre'

urlpatterns = [
    path('', views.index),
]
