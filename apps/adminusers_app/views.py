#import utils
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
#import forms
from .forms import UserCreateForm,UserUpdateForm
#import models
from .models import User
# import mixing
from .mixing_admin import SoloAdmin
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(LoginRequiredMixin,SoloAdmin,CreateView):
    """Clase para crear usuarios"""
    model = User
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy('admin_app:list_user')
    login_url = reverse_lazy('user_app:login')
    


class UserListView(LoginRequiredMixin,SoloAdmin,ListView):
    model = User
    template_name = "users/list_user.html"
    context_object_name = 'users'
    paginate_by = 7
    login_url = reverse_lazy('user_app:login')


class UserUpdateView(LoginRequiredMixin,SoloAdmin,UpdateView):
    model = User
    form_class = UserUpdateForm
    context_object_name = 'user'
    template_name = "users/update_user.html"
    success_url = reverse_lazy('admin_app:list_user')
    login_url = reverse_lazy('user_app:login')



class UserDeleteView(LoginRequiredMixin,SoloAdmin,DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy('admin_app:list_user')
    login_url = reverse_lazy('user_app:login')