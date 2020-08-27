from django.urls import path
from .views import *

app_name = "Articles_app"

urlpatterns=[
    path('',home,name='home'),
    path('<slug:slug>/',articleDetails,name='detials'),
]
