from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
