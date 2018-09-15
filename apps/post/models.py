from django.db import models
from django.conf import settings
from django.contrib import admin

class Article(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()

    upvoted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True, related_name = 'upvoted')
    downvoted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True, related_name = 'downvoted')

    channel = models.ForeignKey('channel.Channel', on_delete = models.CASCADE)

    is_pinned = models.BooleanField(default = False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey('post.Article', on_delete = models.CASCADE)
    parent = models.ForeignKey('post.Comment', on_delete = models.CASCADE, blank = True, null = True)

admin.site.register(Article)
admin.site.register(Comment)
