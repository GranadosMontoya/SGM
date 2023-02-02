from django.urls import path
from .views import *


app_name = 'home_app'
urlpatterns = [
    path('',Index.as_view(),name='index'),
]
