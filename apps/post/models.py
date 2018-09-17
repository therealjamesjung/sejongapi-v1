from django.db import models
from django.conf import settings


class Article(models.Model):
    writer = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    upvoted = models.ManyToManyField('profile.Profile', blank=True, related_name='upvoted')
    downvoted = models.ManyToManyField('profile.Profile', blank=True, related_name='downvoted')

    channel = models.ForeignKey('channel.Channel', on_delete=models.CASCADE)

    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    writer = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey('post.Article', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('post.Comment', on_delete=models.CASCADE, blank=True, null=True, related_name='childs')
