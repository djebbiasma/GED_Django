from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    ROLES=(
        ('user','user'),
        ('moderator','moderator'),
        ('admin','admin')
    )

    email=models.EmailField(unique=True)

    role=models.CharField(max_length=30,choices=ROLES,default='user')

    description=models.TextField(blank=True, default='')

    def __str__(self):
        return self.username