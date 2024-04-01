from django.urls import path
from app2.views import *
app_name='hi'
urlpatterns=[
    path('anu/',anu,name='anu'),
]