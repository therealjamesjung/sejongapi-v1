from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager



class User(AbstractBaseUser):
    email = models.EmailField(max_length=64, unique=True, db_index=True)
    username = models.CharField(max_length=32, unique=True, db_index=True)
    student_id = models.CharField(max_length=16, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'student_id']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
