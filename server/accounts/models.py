from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from roles.models import Role

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE, null = True)
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=128)
    codename = models.CharField(max_length=100, unique=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

