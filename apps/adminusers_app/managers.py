from django.db import models
from django.db.models import Q
from django.contrib.auth.models import BaseUserManager

class USerManager(BaseUserManager,models.Manager):
    
    def listar_usuario(self, palabra):
        consulta = self.filter(
            Q(first_name__icontains = palabra) | 
            Q(last_name__icontains = palabra) |
            Q(id__icontains = palabra) |
            Q(email__icontains = palabra)).order_by('id')
        return consulta