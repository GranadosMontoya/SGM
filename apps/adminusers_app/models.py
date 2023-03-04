from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import USerManager
# Create your models here.

class User(AbstractUser):
    """
    Modelo usuarios con campos extras a los que se tienen por defecto
    """
    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    )
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email','is_superuser']
    
    objects = USerManager()

    def __str__(self):
        return self.first_name + self.email