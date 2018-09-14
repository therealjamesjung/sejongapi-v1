from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser

from apps.profile.models import Profile

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

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)
