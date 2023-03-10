from django.shortcuts import render
from django.views.generic import CreateView
from .models import Products
# Create your views here.


class ProductsCreateView(CreateView):
    model = Products
    template_name = "products/createproducts.html"
    fields = '__all__'