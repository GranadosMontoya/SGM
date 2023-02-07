from django.urls import path
from .views import *


app_name = 'user_app'
urlpatterns = [
    path('login',Login.as_view(),name='login'),
    path('home/',Home.as_view(),name='home'),
    path('logout/',Logout.as_view(),name='logout')
]
