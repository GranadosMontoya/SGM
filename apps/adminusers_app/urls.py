from django.urls import path
from .views import *


app_name = 'admin_app'
urlpatterns = [
    path('create_user/',UserCreateView.as_view(),name='create_user'),
    path('list_user/',UserListView.as_view(),name='list_user'),
    path('update_user/<pk>',UserUpdateView.as_view(),name='update_user'),
    path('delete_user/<pk>', UserDeleteView.as_view(), name='delete_user'),
]
