from django.urls import path
from app1.views import *
app_name='hh'
urlpatterns=[
    path('name/',name,name='name')
]