from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    rules = models.TextField(blank=True)

    moderators = models.ManyToManyField('profile.Profile', related_name='moderators')
    subscribers = models.ManyToManyField('profile.Profile', related_name='subscriptions')
    blacklist = models.ManyToManyField('profile.Profile', related_name='blacklist')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_subscribers(self):
        return self.subscribers

    def add_subscriber(self, profile):
        self.subscribers.add(profile)
        return self.subscribers

    def remove_subscriber(self, profile):
        self.subscribers.remove(profile)
        return self.subscribers
