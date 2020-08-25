from django.urls import path
from .views import *

app_name = "Articles_app"

urlpatterns=[
    path('',home)
]
