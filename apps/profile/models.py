from django.db import models

from apps.utils.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    followers = models.ManyToManyField('profile.Profile', blank=True)

    def __str__(self):
        return self.user.username

    def get_followers(self):
        return self.followers

    def add_follower(self, profile):
        self.followers.add(profile)
        return self.followers

    def remove_follower(self, profile):
        self.followers.remove(profile)
        return self.followers
