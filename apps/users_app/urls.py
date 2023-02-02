from django.urls import path
from .views import *


app_name = 'user_app'
urlpatterns = [
    path('login',Login.as_view(),name='login'),
]
