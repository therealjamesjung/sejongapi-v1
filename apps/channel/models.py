from django.db import models

from apps.utils.models import TimestampedModel

from django.template.defaultfilters import slugify


class Channel(TimestampedModel):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    rules = models.TextField(blank=True)

    slug = models.SlugField(default = slugify(name))

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
