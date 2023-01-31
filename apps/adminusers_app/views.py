from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import UserCreateForm,UserUpdateForm
from .models import User
# Create your views here.


class UserCreateView(CreateView):
    """Clase para crear usuarios"""
    model = User
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = '/'


class UserListView(ListView):
    model = User
    template_name = "users/list_user.html"
    context_object_name = 'users'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update_user.html"
    success_url = reverse_lazy('admin_app:list_user')
