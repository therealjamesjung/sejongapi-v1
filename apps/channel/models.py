from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    rules = models.TextField(blank=True)
    moderators = models.ManyToManyField('profile.Profile', related_name='moderators')

    def __str__(self):
        return self.name
