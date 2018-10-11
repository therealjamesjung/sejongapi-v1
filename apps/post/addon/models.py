from django.db import models


class BaseAddon(models.Model):
    class Meta:
        abstract = True


class ImageAddon(BaseAddon):
    post = models.ForeignKey('post.Article', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='media/')


class VideoAddon(BaseAddon):
    post = models.ForeignKey('post.Article', on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='media/')