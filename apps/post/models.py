from django.db import models
from django.conf import settings

class Post(models.model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()

    upvote = models.IntegerField(default = 0)
    downvote = models.IntegerField(default = 0)

    is_pinned = models.BooleanField(default = False)

    def __str__(self):
        return self.title
