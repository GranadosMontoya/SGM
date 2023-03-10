from django.urls import path
from .views import *


app_name = 'products_app'
urlpatterns = [
    path('create_product/',ProductsCreateView.as_view(),name='create_product'),
]
