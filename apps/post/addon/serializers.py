from rest_framework import serializers

from .models import BaseAddon, ImageAddon, VideoAddon


class BaseAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAddon
        abstract = True


class ImageAddonSerializer(BaseAddonSerializer):
    class Meta:
        model = ImageAddon
        fields = ('image',)


class VideoAddonSerializer(BaseAddonSerializer):
    class Meta:
        model = VideoAddon
        fields = ('video',)
